from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
    ad = models.CharField(max_length=100)

    def __str__(self):
        return self.ad

class Etkinlik(models.Model):
    DURUM_SECENEKLER = [
        ('taslak', 'Taslak'),
        ('yayinda', 'Yayında'),
        ('iptal', 'İptal'),
    ]
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()
    tarih = models.DateTimeField()
    konum = models.CharField(max_length=200)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    organizator = models.ForeignKey(User, on_delete=models.CASCADE)
    durum = models.CharField(max_length=10, choices=DURUM_SECENEKLER, default='taslak')
    olusturulma = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik