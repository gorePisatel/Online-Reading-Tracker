from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='user_settings'),
    path('my-library/', TemplateView.as_view(template_name='library/book_list.html'), name='my_library'),
]
