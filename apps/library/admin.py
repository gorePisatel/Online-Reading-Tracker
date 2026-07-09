from django.contrib.admin import ModelAdmin, display, register

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
        'total_pages',
        'created_by',
        'cover_status',
        'text_status',
    )
    search_fields = ('title', 'author_name',)
    list_filter = ('genre',)
    readonly_fields = ('total_pages',)

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
