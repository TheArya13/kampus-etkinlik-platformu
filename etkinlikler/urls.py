
from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),

    path('etkinlik/<int:pk>/', views.etkinlik_detay, name='etkinlik_detay'),

    path('etkinlik/<int:pk>/kayit/', views.etkinlik_kayit, name='etkinlik_kayit'),

    path('etkinlik/<int:pk>/qr/', views.qr_goster, name='qr_goster'),

    path('etkinlik/<int:pk>/qr-dogrula/', views.qr_dogrula, name='qr_dogrula'),

    path('kulupler/', views.kulup_listesi, name='kulup_listesi'),

    path('kulup/<int:pk>/', views.kulup_detay, name='kulup_detay'),
]
