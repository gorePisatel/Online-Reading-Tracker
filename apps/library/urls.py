from django.urls import path

from . import views


urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/read/', views.book_reader, name='book_reader'),
    path(
        '<int:pk>/read/progress/',
        views.book_reader_progress,
        name='book_reader_progress',
    ),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/update/', views.book_update, name='book_update'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
]
