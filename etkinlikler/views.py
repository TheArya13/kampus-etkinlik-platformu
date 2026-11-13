
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST

from .models import Etkinlik, Kulup, Kayit, Yoklama

import qrcode
import io
import base64
import secrets


# ANA SAYFA
def anasayfa(request):
    etkinlikler = Etkinlik.objects.filter(
        durum='aktif'
    ).order_by('tarih')

    return render(request, 'etkinlikler/anasayfa.html', {
        'etkinlikler': etkinlikler
    })


# ETKİNLİK DETAY
def etkinlik_detay(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)
    kayitli = False

    if request.user.is_authenticated:
        kayitli = Kayit.objects.filter(
            kullanici=request.user,
            etkinlik=etkinlik
        ).exists()

    return render(request, 'etkinlikler/etkinlik_detay.html', {
        'etkinlik': etkinlik,
        'kayitli': kayitli
    })


# ETKİNLİĞE KAYIT
@login_required
def etkinlik_kayit(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)

    if etkinlik.durum != 'aktif':
        messages.error(
            request,
            'Bu etkinlik için kayıt kabul edilmiyor.'
        )
        return redirect('etkinlik_detay', pk=pk)

    if Kayit.objects.filter(
        kullanici=request.user,
        etkinlik=etkinlik
    ).exists():
        messages.info(
            request,
            'Bu etkinliğe zaten kayıtlısınız.'
        )
        return redirect('etkinlik_detay', pk=pk)

    if Kayit.objects.filter(
        etkinlik=etkinlik
    ).count() >= etkinlik.kontenjan:
        messages.error(request, 'Kontenjan dolu.')
        return redirect('etkinlik_detay', pk=pk)

    Kayit.objects.create(
        kullanici=request.user,
        etkinlik=etkinlik,
        qr_kod=secrets.token_urlsafe(16)
    )

    messages.success(
        request,
        'Kayıt işleminiz tamamlandı.'
    )
    return redirect('etkinlik_detay', pk=pk)


# KULÜP LİSTESİ
def kulup_listesi(request):
    kulupler = Kulup.objects.all()

    return render(request, 'etkinlikler/kulup_listesi.html', {
        'kulupler': kulupler
    })


# KULÜP DETAY
def kulup_detay(request, pk):
    kulup = get_object_or_404(Kulup, pk=pk)
    etkinlikler = Etkinlik.objects.filter(kulup=kulup)

    return render(request, 'etkinlikler/kulup_detay.html', {
        'kulup': kulup,
        'etkinlikler': etkinlikler
    })


# QR KODUNU GÖSTER
@login_required
def qr_goster(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)

    kayit = Kayit.objects.filter(
        kullanici=request.user,
        etkinlik=etkinlik
    ).first()

    if kayit is None:
        messages.error(
            request,
            'Bu etkinliğe kayıtlı olmadan QR kod alamazsınız.'
        )
        return redirect('etkinlik_detay', pk=pk)

    if not kayit.qr_kod:
        kayit.qr_kod = secrets.token_urlsafe(16)
        kayit.save(update_fields=['qr_kod'])

    qr = qrcode.make(kayit.qr_kod)

    buffer = io.BytesIO()
    qr.save(buffer, format='PNG')

    qr_base64 = base64.b64encode(
        buffer.getvalue()
    ).decode()

    return render(request, 'etkinlikler/qr_goster.html', {
        'etkinlik': etkinlik,
        'qr_base64': qr_base64,
        'kayit': kayit
    })


# QR DOĞRULAMA VE YOKLAMA
@login_required
@require_POST
def qr_dogrula(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)

    # Yalnızca yetkili kişiler yoklama alabilir.
    if not (
        request.user.is_staff
        or etkinlik.kulup.yonetici_id == request.user.id
    ):
        return HttpResponseForbidden(
            'QR doğrulama yetkiniz yok.'
        )

    token = request.POST.get('qr_kod', '').strip()

    if not token:
        messages.error(request, 'QR kodu boş olamaz.')
        return redirect('etkinlik_detay', pk=pk)

    kayit = Kayit.objects.filter(
        etkinlik=etkinlik,
        qr_kod=token
    ).first()

    if kayit is None:
        messages.error(request, 'Geçersiz QR kodu.')
        return redirect('etkinlik_detay', pk=pk)

    if kayit.katildi:
        messages.info(
            request,
            'Bu katılım zaten kaydedilmiş.'
        )
        return redirect('etkinlik_detay', pk=pk)

    # Katılım bilgisini kaydet.
    kayit.katildi = True
    kayit.save(update_fields=['katildi'])

    # Yoklama kaydını oluştur.
    Yoklama.objects.get_or_create(kayit=kayit)

    messages.success(
        request,
        'QR doğrulandı. Katılım başarıyla kaydedildi.'
    )

    return redirect('etkinlik_detay', pk=pk)
