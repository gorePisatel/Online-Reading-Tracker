from django.urls import path

from apps.library import api_views


urlpatterns = [
    path('', api_views.api_book_list, name='api_book_list'),
    path('create/', api_views.BookCreateAPIView.as_view(), name='api_book_create'),
    path('genres/', api_views.api_genre_list, name='api_genre_list'),
    path('genres/create/', api_views.api_genre_create, name='api_genre_create'),
    path('<int:pk>/', api_views.BookDetailAPIView.as_view(), name='api_book_detail'),
    path('<int:pk>/update/', api_views.BookUpdateDeleteAPIView.as_view(), name='api_book_update'),
    path('<int:pk>/delete/', api_views.BookUpdateDeleteAPIView.as_view(), name='api_book_delete'),
]
