# from django.contrib import admin
# from django.urls import path


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Временный маршрут: связываем твой шаблон напрямую с главной страницей
    path('', TemplateView.as_view(template_name='library/book_list.html'), name='book_list'),
    
    path('auth/', include('apps.users.urls')),
]