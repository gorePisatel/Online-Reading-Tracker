from django.forms import ModelForm

from .models import Book, Genre


class GenreForm(ModelForm):

    class Meta:
        model = Genre
        fields = [
            "name",
        ]


class BookForm(ModelForm):

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