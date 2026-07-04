from django.contrib import admin

from .models import ReadingProgress, Review


@admin.register(ReadingProgress)
class ReadingProgressAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "book",
        "status",
        "current_page",
    )

    list_filter = (
        "status",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "book",
        "rating",
        "created_at",
    )

    list_filter = (
        "rating",
    )