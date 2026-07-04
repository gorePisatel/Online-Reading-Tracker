from django import forms

from .models import Book, Genre


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = [
            "name",
        ]


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            "title",
            "author_name",
            "genre",
            "description",
            "total_pages",
            "cover",
        ]