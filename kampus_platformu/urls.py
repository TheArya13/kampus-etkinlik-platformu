from django.contrib import admin
from django.urls import path
from etkinlikler import views as etkinlik_views
from kullanicilar import views as kullanici_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', etkinlik_views.anasayfa, name='anasayfa'),
    path('etkinlik/<int:pk>/', etkinlik_views.etkinlik_detay, name='etkinlik_detay'),
    path('etkinlik/<int:pk>/kayit/', etkinlik_views.etkinlik_kayit, name='etkinlik_kayit'),
    path('kulupler/', etkinlik_views.kulup_listesi, name='kulup_listesi'),
    path('kulup/<int:pk>/', etkinlik_views.kulup_detay, name='kulup_detay'),
    path('kayit/', kullanici_views.kayit, name='kayit'),
    path('giris/', kullanici_views.giris, name='giris'),
    path('cikis/', kullanici_views.cikis, name='cikis'),
    path('profil/', kullanici_views.profil, name='profil'),
]