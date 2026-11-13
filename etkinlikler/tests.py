
from django.test import TestCase
from django.urls import reverse


class EtkinlikTestleri(TestCase):

    def test_anasayfa_aciliyor(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_qr_giris_gerektirir(self):
        response = self.client.get("/etkinlik/1/qr/")
        self.assertEqual(response.status_code, 302)
