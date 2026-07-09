from django.urls import path

from apps.tracker import api_views


urlpatterns = [
    path('progress/', api_views.ProgressListAPIView.as_view(), name='api_progress_list',),
    path('progress/create/', api_views.ProgressCreateAPIView.as_view(), name='api_progress_create'),
    path('progress/<int:pk>/update/', api_views.ProgressUpdateAPIView.as_view(), name='api_progress_update'),
    path('reviews/', api_views.api_review_list, name='api_review_list'),
    path('reviews/create/', api_views.api_review_create, name='api_review_create'),
]
