from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from guide import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)