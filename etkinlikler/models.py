from django.db import models
from django.contrib.auth.models import User

class Kulup(models.Model):
    ad = models.CharField(max_length=200)
    aciklama = models.TextField()
    kurulus_tarihi = models.DateField()
    logo = models.ImageField(upload_to='kulup_loglari/', blank=True)
    
    def __str__(self):
        return self.ad

class Etkinlik(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()
    tarih = models.DateTimeField()
    konum = models.CharField(max_length=300)
    kulup = models.ForeignKey(Kulup, on_delete=models.CASCADE)
    kontenjan = models.IntegerField(default=50)
    
    def __str__(self):
        return self.baslik

class Kayit(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    etkinlik = models.ForeignKey(Etkinlik, on_delete=models.CASCADE)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    qr_kod = models.CharField(max_length=500, blank=True)
    katildi = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.kullanici} - {self.etkinlik}"