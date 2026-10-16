from django.contrib import admin
from .models import Kulup, Etkinlik, Kayit, Yoklama

@admin.register(Kulup)
class KulupAdmin(admin.ModelAdmin):
    list_display = ['ad', 'yonetici', 'kurulus_tarihi']
    search_fields = ['ad']

@admin.register(Etkinlik)
class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'kulup', 'tarih', 'konum', 'kontenjan', 'durum']
    list_filter = ['durum', 'kulup']
    search_fields = ['baslik']

@admin.register(Kayit)
class KayitAdmin(admin.ModelAdmin):
    list_display = ['kullanici', 'etkinlik', 'kayit_tarihi', 'katildi']
    list_filter = ['katildi']

@admin.register(Yoklama)
class YoklamaAdmin(admin.ModelAdmin):
    list_display = ['kayit']