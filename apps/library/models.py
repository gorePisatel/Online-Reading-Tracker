from django.db.models import (
    Model,
    CASCADE,
    CharField,
    ForeignKey,
    TextField,
    PositiveIntegerField,
    ImageField,
    DateTimeField
)
from django.conf import settings


class Genre(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(Model):
    title = CharField(max_length=255)
    author_name = CharField(max_length=255)
    genre = ForeignKey(Genre, on_delete=CASCADE)
    description = TextField()
    text = TextField(blank=True)
    total_pages = PositiveIntegerField()

    cover = ImageField(upload_to='covers/', blank=True, null=True)

    created_by = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
