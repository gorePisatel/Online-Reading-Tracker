from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    description = models.TextField()

    total_pages = models.PositiveIntegerField()

    cover = models.ImageField(
        upload_to="covers/",
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title