from django.db import models
from django.conf import settings

from apps.library.models import Book


class ReadingProgress(models.Model):

    STATUS_CHOICES = [
        ("want_to_read", "Want to Read"),
        ("reading", "Reading"),
        ("completed", "Completed"),
        ("dropped", "Dropped"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="want_to_read",
    )

    current_page = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    @property
    def progress_percent(self):
        return int(
            (self.current_page / self.book.total_pages) * 100
        )

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class Review(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    rating = models.PositiveIntegerField()

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.book.title} - {self.rating}"