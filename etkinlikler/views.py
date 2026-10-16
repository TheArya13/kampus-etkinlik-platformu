from django.shortcuts import render
from .models import Etkinlik

def anasayfa(request):
    etkinlikler = Etkinlik.objects.all()
    return render(request, 'etkinlikler/anasayfa.html', {'etkinlikler': etkinlikler})