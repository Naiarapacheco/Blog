from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('content/', include('content.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Adiciona URLs do CKEditor
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)