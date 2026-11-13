from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Etkinlik, Kulup, Kayit
import qrcode
import io
import base64
import secrets
from django.contrib import messages

def anasayfa(request):
    etkinlikler = Etkinlik.objects.filter(durum='aktif').order_by('tarih')
    return render(request, 'etkinlikler/anasayfa.html', {'etkinlikler': etkinlikler})

def etkinlik_detay(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)
    kayitli = False
    if request.user.is_authenticated:
        kayitli = Kayit.objects.filter(kullanici=request.user, etkinlik=etkinlik).exists()
    return render(request, 'etkinlikler/etkinlik_detay.html', {
        'etkinlik': etkinlik,
        'kayitli': kayitli
    })

@login_required
def etkinlik_kayit(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)

    if etkinlik.durum != 'aktif':
        messages.error(request, 'Bu etkinlik için kayıt kabul edilmiyor.')
        return redirect('etkinlik_detay', pk=pk)

    if Kayit.objects.filter(kullanici=request.user, etkinlik=etkinlik).exists():
        messages.info(request, 'Bu etkinliğe zaten kayıtlısınız.')
        return redirect('etkinlik_detay', pk=pk)

    if Kayit.objects.filter(etkinlik=etkinlik).count() >= etkinlik.kontenjan:
        messages.error(request, 'Kontenjan dolu.')
        return redirect('etkinlik_detay', pk=pk)

    Kayit.objects.create(
        kullanici=request.user,
        etkinlik=etkinlik,
        qr_kod=secrets.token_urlsafe(16),
    )
    messages.success(request, 'Kayıt işleminiz tamamlandı.')
    return redirect('etkinlik_detay', pk=pk)
    return redirect('etkinlik_detay', pk=pk)

def kulup_listesi(request):
    kulupler = Kulup.objects.all()
    return render(request, 'etkinlikler/kulup_listesi.html', {'kulupler': kulupler})

def kulup_detay(request, pk):
    kulup = get_object_or_404(Kulup, pk=pk)
    etkinlikler = Etkinlik.objects.filter(kulup=kulup)
    return render(request, 'etkinlikler/kulup_detay.html', {
        'kulup': kulup,
        'etkinlikler': etkinlikler
    })
@login_required
def qr_goster(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)
    kayit = Kayit.objects.filter(kullanici=request.user, etkinlik=etkinlik).first()
    
    qr_data = f"Etkinlik: {etkinlik.baslik} | Kullanici: {request.user.username} | ID: {pk}"
    qr = qrcode.make(qr_data)
    
    buffer = io.BytesIO()
    qr.save(buffer, format='PNG')
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return render(request, 'etkinlikler/qr_goster.html', {
        'etkinlik': etkinlik,
        'qr_base64': qr_base64,
        'kayit': kayit,
    })