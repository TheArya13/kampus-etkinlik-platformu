from django.shortcuts import render, get_object_or_404
from .models import Etkinlik, Kategori
from django.contrib.auth.decorators import login_required

def etkinlik_listesi(request):
    etkinlikler = Etkinlik.objects.filter(durum='yayinda')
    return render(request, 'events/etkinlik_listesi.html', {'etkinlikler': etkinlikler})

def etkinlik_detay(request, pk):
    etkinlik = get_object_or_404(Etkinlik, pk=pk)
    return render(request, 'events/etkinlik_detay.html', {'etkinlik': etkinlik})
def anasayfa(request):
    etkinlikler = Etkinlik.objects.filter(durum='yayinda')
    return render(request, 'events/etkinlik_listesi.html', {'etkinlikler': etkinlikler})

def etkinlik_kayit(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'events/erisim_hatasi.html', status=403)
    etkinlik = get_object_or_404(Etkinlik, pk=pk)
    return render(request, 'events/etkinlik_detay.html', {'etkinlik': etkinlik})

def kulup_listesi(request):
    return render(request, 'events/etkinlik_listesi.html', {})

def kulup_detay(request, pk):
    return render(request, 'events/etkinlik_detay.html', {})