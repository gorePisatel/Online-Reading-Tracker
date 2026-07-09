from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.library.urls')),
    path('auth/', include('apps.users.urls')),
    path('my-library/', include('apps.tracker.urls')),

    path('api/users/', include('apps.users.api_urls')),
    path('api/books/', include('apps.library.api_urls')),
    path('api/tracker/', include('apps.tracker.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
