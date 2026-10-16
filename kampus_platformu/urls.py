from django.contrib import admin
from django.urls import path
from etkinlikler import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.anasayfa, name='anasayfa'),
]