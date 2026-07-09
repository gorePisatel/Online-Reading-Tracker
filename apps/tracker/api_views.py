from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tracker.models import ReadingProgress, Review
from apps.tracker.serializers import (
    ReadingProgressSerializer,
    ReviewCreateSerializer,
    ReviewSerializer,
)


class ProgressListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        progress_items = ReadingProgress.objects.select_related('book').filter(
            user=request.user,
        )
        serializer = ReadingProgressSerializer(
            progress_items,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProgressCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReadingProgressSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            progress = serializer.save(user=request.user)
            return Response(
                ReadingProgressSerializer(
                    progress,
                    context={'request': request},
                ).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgressUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        progress = get_object_or_404(
            ReadingProgress,
            pk=pk,
            user=request.user,
        )
        serializer = ReadingProgressSerializer(
            progress,
            data=request.data,
            partial=True,
            context={'request': request},
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_review_list(request):
    reviews = Review.objects.select_related('book', 'user').all()
    serializer = ReviewSerializer(
        reviews,
        many=True,
        context={'request': request},
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_review_create(request):
    serializer = ReviewCreateSerializer(data=request.data)

    if serializer.is_valid():
        review = Review.objects.create(
            user=request.user,
            book=serializer.validated_data['book'],
            rating=serializer.validated_data['rating'],
            text=serializer.validated_data['text'],
        )
        return Response(
            ReviewSerializer(review, context={'request': request}).data,
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
