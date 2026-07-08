from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.library.models import Book, Genre
from apps.tracker.models import ReadingProgress
from apps.library.forms import BookForm


def book_list(request):
    books = Book.objects.select_related("genre").order_by("title")
    genres = Genre.objects.all().order_by("name")

    search = request.GET.get("search", "").strip()
    selected_genre_id = request.GET.get("genre", "").strip()

    if search:
        books = books.filter(title__icontains=search)

    if selected_genre_id and selected_genre_id.isdigit():
        books = books.filter(genre_id=int(selected_genre_id))
    else:
        selected_genre_id = ""

    user_progress = []

    if request.user.is_authenticated:
        user_progress = (
            ReadingProgress.objects
            .filter(user=request.user, status="reading")
            .select_related("book", "book__genre")
            .order_by("-updated_at")[:6]
        )

    context = {
        "books": books,
        "genres": genres,
        "user_progress": user_progress,
        "selected_genre_id": selected_genre_id,
        "search_query": search,
    }

    return render(request, "library/book_list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    context = {
        "book": book,
    }

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

    context = {
        "form": form,
    }

    return render(request, "library/book_form.html", context)


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()

            messages.success(request, "Book updated successfully.")
            return redirect("book_detail", pk=book.id)

    else:
        form = BookForm(instance=book)

    context = {
        "book": book,
        "form": form,
    }

    return render(request, "library/book_form.html", context)


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()

        messages.success(request, "Book deleted successfully.")
        return redirect("book_list")

    context = {
        "book": book,
    }

    return render(request, "library/book_confirm_delete.html", context)