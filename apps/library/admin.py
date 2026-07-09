from django.contrib.admin import display, register, ModelAdmin

from .models import Genre, Book


@register(Genre)
class GenreAdmin(ModelAdmin):

    list_display = ('id', 'name',)


@register(Book)
class BookAdmin(ModelAdmin):

    list_display = (
        'title',
        'author_name',
        'genre',
        'created_by',
        'cover_status',
        'text_status',
    )
    search_fields = ('title', 'author_name',)
    list_filter = ('genre',)

    @display(description='Cover')
    def cover_status(self, obj):
        if obj.cover:
            return 'Yes'
        return 'No'

    @display(description='Text')
    def text_status(self, obj):
        if obj.text.strip():
            return 'Yes'
        return 'No'
