from django.db.models import (
    CharField,
    PositiveIntegerField,
    DateTimeField,
    ForeignKey,
    TextField,
    Model,
    CASCADE,
)
from django.conf import settings

from apps.library.models import Book


class ReadingProgress(Model):

    STATUS_CHOICES = [
        ('want_to_read', 'Want to Read'),
        ('reading', 'Reading'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]

    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE,)
    book = ForeignKey(Book, on_delete=CASCADE,)
    status = CharField(max_length=20, choices=STATUS_CHOICES, default='want_to_read',)
    current_page = PositiveIntegerField(default=0)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def progress_percent(self):
        if not self.book.total_pages:
            return 0
        return int((self.current_page / self.book.total_pages) * 100)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'


class Review(Model):

    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE,)
    book = ForeignKey(Book, on_delete=CASCADE,)
    rating = PositiveIntegerField()
    text = TextField()

    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} - {self.rating}'
