from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Book, Genre
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    genres = Genre.objects.all()

    search = request.GET.get("search")
    genre = request.GET.get("genre")

    if search:
        books = books.filter(title__icontains=search)

    if genre:
        books = books.filter(genre_id=genre)

    context = {
        "books": books,
        "genres": genres,
    }

    return render(
        request,
        "library/book_list.html",
        context
    )


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)

    return render(
        request,
        "library/book_detail.html",
        {
            "book": book
        }
    )


@login_required
def book_create(request):

    if request.method == "POST":

        form = BookForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            book = form.save(commit=False)

            book.created_by = request.user

            book.save()

            messages.success(
                request,
                "Book created successfully."
            )

            return redirect(
                "book_list"
            )

    else:
        form = BookForm()

    return render(
        request,
        "library/book_form.html",
        {
            "form": form
        }
    )


@login_required
def book_update(request, pk):

    book = get_object_or_404(
        Book,
        id=pk
    )

    if request.method == "POST":

        form = BookForm(
            request.POST,
            request.FILES,
            instance=book
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Book updated successfully."
            )

            return redirect(
                "book_detail",
                pk=book.id
            )

    else:

        form = BookForm(
            instance=book
        )

    return render(
        request,
        "library/book_form.html",
        {
            "form": form
        }
    )


@login_required
def book_delete(request, pk):

    book = get_object_or_404(
        Book,
        id=pk
    )

    if request.method == "POST":

        book.delete()

        messages.success(
            request,
            "Book deleted successfully."
        )

        return redirect(
            "book_list"
        )

    return render(
        request,
        "library/book_confirm_delete.html",
        {
            "book": book
        }
    )