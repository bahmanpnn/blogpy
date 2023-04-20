from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('',include('blog.urls')),
    path('api/',include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

from django.conf.urls.static import static
from django.conf import settings

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#     urlpatterns += static('contact-us/static/',document_root=settings.STATIC_ROOT)
