from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView  # Импортируем для временных заглушек

urlpatterns = [
    # Рабочие маршруты для входа и выхода
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Временные заглушки, чтобы шаблоны не выдавали ошибку NoReverseMatch:
    path('register/', TemplateView.as_view(template_name='users/register.html'), name='register'),
    path('my-library/', TemplateView.as_view(template_name='library/book_list.html'), name='my_library'),
]