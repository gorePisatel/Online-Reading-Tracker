from django.urls import path

from . import views


urlpatterns = [
    path('', views.my_library, name='my_library'),
    path('add/<int:pk>/', views.add_to_library, name='add_to_library'),
    path('progress/<int:pk>/', views.update_progress, name='update_progress'),
    path('review/<int:pk>/', views.create_review, name='create_review'),
]
