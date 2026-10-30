from django.urls import path
from . import views

urlpatterns = [
    path('etkinlikler/', views.etkinlik_listesi, name='etkinlik_listesi'),
    path('etkinlik/<int:pk>/', views.etkinlik_detay, name='etkinlik_detay'),
]