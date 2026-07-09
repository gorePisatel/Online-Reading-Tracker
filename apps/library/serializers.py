from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    Serializer,
    IntegerField,
    ValidationError,
)

from apps.library.models import Book, Genre


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(ModelSerializer):
    genre_name = CharField(source='genre.name', read_only=True)
    created_by_username = CharField(
        source='created_by.username',
        read_only=True,
    )

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author_name',
            'genre',
            'genre_name',
            'description',
            'total_pages',
            'cover',
            'created_by',
            'created_by_username',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'created_by',
            'created_by_username',
            'created_at',
            'updated_at',
        ]


class BookSearchSerializer(Serializer):
    search = CharField(required=False, allow_blank=True)
    genre = IntegerField(required=False)

    def validate_genre(self, value):
        if not Genre.objects.filter(id=value).exists():
            raise ValidationError('Genre does not exist.')
        return value
