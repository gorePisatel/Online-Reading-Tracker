from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ReadingProgress, Review
from .forms import ReadingProgressForm, ReviewForm
from apps.library.models import Book


@login_required
def my_library(request):
    books = ReadingProgress.objects.filter(user=request.user)
    context = {'library_items': books}

    return render(request, 'tracker/my_library.html', context)


@login_required
def add_to_library(request, pk):
    book = get_object_or_404(Book, id=pk)
    ReadingProgress.objects.get_or_create(user=request.user, book=book)

    messages.success(request, 'Book added to your library.')
    return redirect('my_library')


@login_required
def update_progress(request, pk):
    progress = get_object_or_404(ReadingProgress,id=pk, user=request.user)

    if request.method == 'POST':
        form = ReadingProgressForm(request.POST, instance=progress)

        if form.is_valid():
            form.save()

            messages.success(request, 'Progress updated.')
            return redirect('my_library')

    else:
        form = ReadingProgressForm(instance=progress)

    context = {'form': form}

    return render(request, 'tracker/progress_form.html', context)


@login_required
def create_review(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)

            review.user = request.user
            review.book = book
            review.save()

            messages.success(request, 'Review added successfully.')
            return redirect('book_detail', pk=book.id)

    else:
        form = ReviewForm()

    context = {
        'form': form,
        'book': book,
        }

    return render(request, 'tracker/review_form.html', context)
