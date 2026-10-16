from django.contrib import admin
from django.urls import path
from etkinlikler import views as etkinlik_views
from kullanicilar import views as kullanici_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', etkinlik_views.anasayfa, name='anasayfa'),
    path('kayit/', kullanici_views.kayit, name='kayit'),
    path('giris/', kullanici_views.giris, name='giris'),
    path('cikis/', kullanici_views.cikis, name='cikis'),
]