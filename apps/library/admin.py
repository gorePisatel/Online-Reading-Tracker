from django.contrib.admin import register, ModelAdmin

from .models import Genre, Book


@register(Genre)
class GenreAdmin(ModelAdmin):

    list_display = ("id", "name",)


@register(Book)
class BookAdmin(ModelAdmin):

    list_display = (
        "title",
        "author_name",
        "genre",
        "created_by",
    )
    search_fields = ("title", "author_name",)
    list_filter = ("genre",)