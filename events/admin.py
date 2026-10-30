from django.contrib import admin
from .models import Kategori, Etkinlik

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ['ad']

@admin.register(Etkinlik)
class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tarih', 'kategori', 'organizator', 'durum']
    list_filter = ['durum', 'kategori']