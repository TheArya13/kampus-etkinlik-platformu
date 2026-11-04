from django.shortcuts import render, get_object_or_404
from .models import Etkinlik, Kategori
from django.contrib.auth.decorators import login_required
import qrcode
import io
import base64

def etkinlik_listesi(request):
    etkinlikler = Etkinlik.objects.filter(durum='yayinda')
    return render(request, 'events/etkinlik_listesi.html', {'etkinlikler': etkinlikler})

def etkinlik_detay(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)
    return render(request, 'events/etkinlik_detay.html', {'etkinlik': etkinlik})
def anasayfa(request):
    etkinlikler = Etkinlik.objects.filter(durum='yayinda')
    return render(request, 'etkinlikler/anasayfa.html', {'etkinlikler': etkinlikler})

def etkinlik_kayit(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'events/erisim_hatasi.html', status=403)
    etkinlik = get_object_or_404(Etkinlik, pk=pk)
    return render(request, 'events/etkinlik_detay.html', {'etkinlik': etkinlik})

def kulup_listesi(request):
    return render(request, 'events/etkinlik_listesi.html', {})

def kulup_detay(request, pk):
    return render(request, 'events/etkinlik_detay.html', {})

def qr_goster(request, pk):
    from events.models import Etkinlik
    from etkinlikler.models import Kayit
    etkinlik = get_object_or_404(Etkinlik, pk=pk)
    kayit = Kayit.objects.filter(kullanici=request.user, etkinlik__pk=pk).first()
    
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