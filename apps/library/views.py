import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from apps.library.forms import BookForm
from apps.library.models import Book, Genre, WORDS_PER_READER_PAGE
from apps.tracker.forms import ReviewForm
from apps.tracker.models import ReadingProgress, Review


def can_manage_books(user):
    return (
        user.is_authenticated
        and (
            user.is_staff
            or getattr(user, 'is_admin', False)
            or getattr(user, 'is_moderator', False)
        )
    )


def book_list(request):
    books = Book.objects.select_related('genre').order_by('title')
    genres = Genre.objects.all().order_by('name')

    search = request.GET.get('search', '').strip()
    selected_genre_id = request.GET.get('genre', '').strip()

    if search:
        books = books.filter(title__icontains=search)

    if selected_genre_id and selected_genre_id.isdigit():
        books = books.filter(genre_id=int(selected_genre_id))
    else:
        selected_genre_id = ''

    user_progress = []

    if request.user.is_authenticated:
        user_progress = (
            ReadingProgress.objects
            .filter(user=request.user, status='reading')
            .select_related('book', 'book__genre')
            .order_by('-updated_at')[:6]
        )

    context = {
        'books': books,
        'genres': genres,
        'user_progress': user_progress,
        'selected_genre_id': selected_genre_id,
        'search_query': search,
    }

    return render(request, 'library/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = (
        Review.objects
        .filter(book=book)
        .select_related('user')
        .order_by('-created_at')
    )
    rating_stats = reviews.aggregate(
        average_rating=Avg('rating'),
        review_count=Count('id'),
    )
    average_rating = rating_stats['average_rating']
    rating_value = round(average_rating, 1) if average_rating else None
    rating_rounded = int(average_rating + 0.5) if average_rating else 0
    user_progress = None

    if request.user.is_authenticated:
        user_progress = ReadingProgress.objects.filter(
            user=request.user,
            book=book,
        ).first()

    context = {
        'book': book,
        'reviews': reviews,
        'review_form': ReviewForm(),
        'review_count': rating_stats['review_count'],
        'rating_value': rating_value,
        'rating_rounded': rating_rounded,
        'rating_stars': range(1, 6),
        'user_progress': user_progress,
        'can_manage_books': can_manage_books(request.user),
    }

    return render(request, 'library/book_detail.html', context)


@login_required
def book_create(request):
    if not can_manage_books(request.user):
        messages.error(request, 'Only staff members can create catalog books.')
        return redirect('book_list')

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()

            messages.success(request, 'Book created successfully.')

            return redirect('book_list')

    else:
        form = BookForm()

    context = {
        'form': form,
    }

    return render(request, 'library/book_form.html', context)


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if not can_manage_books(request.user):
        messages.error(request, 'Only staff members can edit catalog books.')
        return redirect('book_detail', pk=book.id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully.')

            return redirect('book_detail', pk=book.id)

    else:
        form = BookForm(instance=book)

    context = {
        'book': book,
        'form': form,
    }

    return render(request, 'library/book_form.html', context)


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if not can_manage_books(request.user):
        messages.error(request, 'Only staff members can delete catalog books.')
        return redirect('book_detail', pk=book.id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully.')

        return redirect('book_list')

    context = {'book': book}

    return render(request, 'library/book_confirm_delete.html', context)


def book_reader(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user_progress = None

    if request.user.is_authenticated:
        user_progress, _ = ReadingProgress.objects.get_or_create(
            user=request.user,
            book=book,
            defaults={
                'status': 'reading',
                'current_page': 1,
            },
        )

        changed_fields = []

        if user_progress.status == 'want_to_read':
            user_progress.status = 'reading'
            changed_fields.append('status')

        if user_progress.current_page < 1:
            user_progress.current_page = 1
            changed_fields.append('current_page')

        if user_progress.current_page > book.total_pages:
            user_progress.current_page = book.total_pages
            changed_fields.append('current_page')

        if changed_fields:
            user_progress.save(
                update_fields=[*set(changed_fields), 'updated_at'],
            )

    text = book.text.strip()

    words = text.split()

    pages = []

    for i in range(0, len(words), WORDS_PER_READER_PAGE):
        page = ' '.join(words[i:i + WORDS_PER_READER_PAGE])
        pages.append(page)

    if not pages:
        pages = ['The text of the book has not been added yet.']

    return render(
        request,
        'library/book_reader.html',
        {
            'book': book,
            'pages': pages,
            'start_page_index': (
                user_progress.current_page - 1
                if user_progress
                else 0
            ),
        },
    )


@login_required
@require_POST
def book_reader_progress(request, pk):
    book = get_object_or_404(Book, pk=pk)

    try:
        payload = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'ok': False, 'error': 'Invalid JSON.'}, status=400)

    try:
        current_page = int(payload.get('current_page'))
    except (TypeError, ValueError):
        return JsonResponse(
            {'ok': False, 'error': 'Invalid current page.'},
            status=400,
        )

    current_page = max(1, min(current_page, book.total_pages))
    progress, _ = ReadingProgress.objects.get_or_create(
        user=request.user,
        book=book,
        defaults={'status': 'reading'},
    )
    progress.current_page = current_page

    if progress.status == 'want_to_read':
        progress.status = 'reading'

    progress.save(update_fields=['current_page', 'status', 'updated_at'])

    return JsonResponse({
        'ok': True,
        'current_page': progress.current_page,
        'total_pages': book.total_pages,
    })
