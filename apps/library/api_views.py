from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.library.models import Book, Genre
from apps.library.serializers import (
    BookSearchSerializer,
    BookSerializer,
    GenreSerializer,
)


def can_manage_books(user):
    return (
        user.is_authenticated
        and (
            user.is_staff
            or getattr(user, 'is_admin', False)
            or getattr(user, 'is_moderator', False)
        )
    )


class CanManageBooks(BasePermission):
    def has_permission(self, request, view):
        return can_manage_books(request.user)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_book_list(request):
    search_serializer = BookSearchSerializer(data=request.query_params)
    search_serializer.is_valid(raise_exception=True)

    books = Book.objects.select_related('genre', 'created_by').all()
    search = search_serializer.validated_data.get('search')
    genre = search_serializer.validated_data.get('genre')

    if search:
        books = books.filter(title__icontains=search)

    if genre:
        books = books.filter(genre_id=genre)

    serializer = BookSerializer(
        books,
        many=True,
        context={'request': request},
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        book = get_object_or_404(
            Book.objects.select_related('genre', 'created_by'),
            pk=pk,
        )
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCreateAPIView(APIView):
    permission_classes = [CanManageBooks]

    def post(self, request):
        serializer = BookSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            book = serializer.save(created_by=request.user)
            return Response(
                BookSerializer(book, context={'request': request}).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateDeleteAPIView(APIView):
    permission_classes = [CanManageBooks]

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(
            book,
            data=request.data,
            partial=True,
            context={'request': request},
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([CanManageBooks])
def api_genre_create(request):
    serializer = GenreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
