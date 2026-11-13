# 🎓 Kampüs Etkinlik ve Kulüp Yönetim Platformu

Bingöl Üniversitesi Bilişim Teknolojileri MYO
Bilgisayar Uygulamaları I - Proje P17

## 🚀 Proje Hakkında

Öğrencilerin kampüs etkinliklerine kayıt olabileceği, kulüpleri takip edebileceği ve QR kod ile yoklama yapılabileceği bir web platformu.

## 🛠️ Kullanılan Teknolojiler

- Python 3.x
- Django 4.x
- SQLite
- Bootstrap 5
- HTML/CSS

## ⚙️ Kurulum

```bash
# Projeyi klonla
git clone https://github.com/TheArya13/kampus-etkinlik-platformu.git

# Dizine gir
cd kampus-etkinlik-platformu

# Bağımlılıkları yükle
pip install django pillow qrcode[pil]

# Veritabanını oluştur
python manage.py migrate

# Sunucuyu başlat
python manage.py runserver
```

## ✅ Tamamlanan Haftalar

| Hafta | Konu | Durum |
|-------|------|-------|
| Hafta 3 | Kurulum, Mimari ve Veri Modeli | ✅ Tamamlandı |
| Hafta 4 | Veritabanı Tasarımı ve Admin Paneli | ✅ Tamamlandı |
| Hafta 5 | Kullanıcı Yönetimi ve Kimlik Doğrulama | ✅ Tamamlandı |
| Hafta 6 | Etkinlik Yönetimi Modülü | ✅ Tamamlandı |
| Hafta 7 | Kayıt ve QR Yoklama Modülü | ✅ Tamamlandı |

## 🔗 Özellikler

- Kulüp ve etkinlik listeleme
- Etkinliğe kayıt olma
- Kullanıcı kayıt /

- 
## Hafta 8 – Vize: Ara Sürüm ve Entegrasyon

### Yapılan Çalışmalar
- Django projesinin sistem kontrolü yapıldı.
- Ana sayfa ve etkinlik detay sayfası test edildi.
- Etkinlik kaydı sonrasında QR kodunun görüntülendiği doğrulandı.
- Giriş yapmayan kullanıcıların QR sayfasına erişemediği kontrol edildi.
- Veritabanı migration durumları kontrol edildi.
- İki otomatik test yazıldı ve başarıyla çalıştırıldı.
- GitHub üzerinde v0.8.0 ara sürüm etiketi oluşturuldu.

### Test Sonuçları
- Django sistem kontrolü: Başarılı
- Ana sayfa testi: Başarılı
- QR giriş koruması testi: Başarılı
- Otomatik testler: 2 test, 2 başarılı

### Devam Eden Çalışmalar
- QR kodunun okutularak doğrulanması
- Etkinlik katılımının yoklama olarak kaydedilmesi
- Modüllerin uçtan uca entegrasyon testlerinin genişletilmesi

### Ara Sürüm
Sürüm: v0.8.0
Branch: kayit-akisi

