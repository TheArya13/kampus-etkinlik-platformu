
from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    ROL_SECENEKLER = [
        ('ogrenci', 'Öğrenci'),
        ('kulup_yoneticisi', 'Kulüp Yöneticisi'),
        ('admin', 'Admin'),
    ]
    kullanici = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROL_SECENEKLER, default='ogrenci')
    bio = models.TextField(blank=True)
    profil_resmi = models.ImageField(upload_to='profil_resimleri/', blank=True)

    def __str__(self):
        return f"{self.kullanici.username} - {self.rol}"