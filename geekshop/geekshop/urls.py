from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from geekshop import settings
from mainapp import views


urlpatterns = [
    path('', views.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', views.contact, name='contact'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('admin/', include('adminapp.urls', namespace='admin'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)