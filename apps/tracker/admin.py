from django.contrib.admin import ModelAdmin, register

from .models import ReadingProgress, Review


@register(ReadingProgress)
class ReadingProgressAdmin(ModelAdmin):

    list_display = (
        'user',
        'book',
        'status',
        'current_page',
    )
    list_filter = ('status',)


@register(Review)
class ReviewAdmin(ModelAdmin):

    list_display = (
        'user',
        'book',
        'rating',
        'created_at',
    )
    list_filter = ('rating',)