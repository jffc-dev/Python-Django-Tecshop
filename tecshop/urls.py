"""
tecshop URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    url(r'^api/', include('aplicacion.urls')),
    url(r'^api/', include('pagina.urls')),
    url(r'^auth/',obtain_auth_token )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
