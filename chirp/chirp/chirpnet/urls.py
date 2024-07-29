# chirp/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chirpnet_list, name='chirpnet_list'),
    path('register/', views.register, name='register'),
    path('create/', views.chirpnet_create, name='chirpnet_create'),
    path('edit/<int:chirpnet_id>/', views.chirpnet_edit, name='chirpnet_form'),
    path('delete/<int:chirpnet_id>/', views.chirpnet_delete, name='chirpnet_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
