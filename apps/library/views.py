from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.library.models import Book, Genre
from apps.tracker.models import ReadingProgress
from apps.library.forms import BookForm


def book_list(request):
    books = Book.objects.select_related("genre").all()
    genres = Genre.objects.all()

    search = request.GET.get("search")
    genre = request.GET.get("genre")

    if search:
        books = books.filter(title__icontains=search)

    if genre:
        books = books.filter(genre_id=genre)

    books_by_genre = []
    for genre_item in genres:
        genre_books = books.filter(genre=genre_item)
        if genre_books.exists():
            books_by_genre.append((genre_item, genre_books[:6]))

    user_progress = []
    if request.user.is_authenticated:

        user_progress = (
            ReadingProgress.objects
            .filter(user=request.user, status="reading")
            .select_related("book", "book__genre")[:6]
        )

    context = {
        "books": books,
        "genres": genres,
        "books_by_genre": books_by_genre,
        "user_progress": user_progress,
        "selected_genre": genre,
        "search_query": search or "",
    }

    return render(request, "library/book_list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    context = {"book": book}

    return render(request, "library/book_detail.html", context)


@login_required
def book_create(request):

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()

            messages.success(request, "Book created successfully.")
            return redirect("book_list")

    else:
        form = BookForm()

    context = {"form": form}

    return render(request, "library/book_form.html", context)


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()

            messages.success(request, "Book updated successfully.")
            return redirect("book_detail", pk=book.id)

    else:
        form = BookForm(instance=book)

    context = {"book": book}

    return render(request, "library/book_form.html", context)


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == "POST":
        book.delete()

        messages.success(request, "Book deleted successfully.")
        return redirect("book_list")

    context = {"book": book}

    return render(request, "library/book_confirm_delete.html", context)


def book_detail(request, pk):

    book = get_object_or_404(
        Book,
        pk=pk
    )

    return render(
        request,
        "library/book_detail.html",
        {
            "book": book
        }
    )
