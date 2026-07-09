from django.urls import path

from apps.users import api_views


urlpatterns = [
    path('register/', api_views.RegisterAPIView.as_view(), name='api_register'),
    path('login/', api_views.LoginAPIView.as_view(), name='api_login'),
    path('logout/', api_views.LogoutAPIView.as_view(), name='api_logout'),
    path('me/', api_views.PersonalInfoAPIView.as_view(), name='api_me'),
    path(
        'me/update/',
        api_views.UpdateProfileAPIView.as_view(),
        name='api_update_profile',
    ),
]
