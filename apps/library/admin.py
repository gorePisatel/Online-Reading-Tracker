from django.contrib import admin

from .models import Genre, Book


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author_name",
        "genre",
        "created_by",
    )

    search_fields = (
        "title",
        "author_name",
    )

    list_filter = (
        "genre",
    )