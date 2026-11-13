from django.contrib import admin
from django.urls import path, include
from kullanicilar import views as kullanici_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('etkinlikler.urls')),
    path('kayit/', kullanici_views.kayit, name='kayit'),
    path('giris/', kullanici_views.giris, name='giris'),
    path('cikis/', kullanici_views.cikis, name='cikis'),
    path('profil/', kullanici_views.profil, name='profil'),
]
