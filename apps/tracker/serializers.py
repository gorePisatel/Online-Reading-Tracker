from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    IntegerField,
    ValidationError,
)

from apps.library.models import Book
from apps.tracker.models import ReadingProgress, Review


class ReadingProgressSerializer(ModelSerializer):
    book_title = CharField(source='book.title', read_only=True)
    progress_percent = IntegerField(read_only=True)

    class Meta:
        model = ReadingProgress
        fields = [
            'id',
            'book',
            'book_title',
            'status',
            'current_page',
            'progress_percent',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'book_title',
            'progress_percent',
            'created_at',
            'updated_at',
        ]

    def validate(self, attrs):
        book = attrs.get('book')

        if self.instance:
            book = book or self.instance.book

        current_page = attrs.get('current_page')

        if current_page is None and self.instance:
            current_page = self.instance.current_page

        if book and current_page is not None and current_page > book.total_pages:
            raise ValidationError(
                'Current page cannot be greater than total pages.'
            )

        request = self.context.get('request')
        if request and request.user.is_authenticated and not self.instance:
            exists = ReadingProgress.objects.filter(
                user=request.user,
                book=book,
            ).exists()

            if exists:
                raise ValidationError(
                    'This book is already in your library.'
                )

        return attrs


class ReviewSerializer(ModelSerializer):
    book_title = CharField(source='book.title', read_only=True)
    username = CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'book',
            'book_title',
            'username',
            'rating',
            'text',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'book_title',
            'username',
            'created_at',
        ]


class ReviewCreateSerializer(Serializer):
    book = IntegerField()
    rating = IntegerField(min_value=1, max_value=5)
    text = CharField()

    def validate_book(self, value):
        try:
            return Book.objects.get(id=value)
        except Book.DoesNotExist as exc:
            raise ValidationError('Book does not exist.') from exc

    def validate_text(self, value):
        value = value.strip()

        if not value:
            raise ValidationError('Review text cannot be empty.')

        return value
