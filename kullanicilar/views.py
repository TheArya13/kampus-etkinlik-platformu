from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profil

def kayit(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profil.objects.create(kullanici=user)
            login(request, user)
            return redirect('anasayfa')
    else:
        form = UserCreationForm()
    return render(request, 'kullanicilar/kayit.html', {'form': form})

def giris(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('anasayfa')
    else:
        form = AuthenticationForm()
    return render(request, 'kullanicilar/giris.html', {'form': form})

def cikis(request):
    logout(request)
    return redirect('anasayfa')

@login_required
def profil(request):
    profil, created = Profil.objects.get_or_create(kullanici=request.user)
    return render(request, 'kullanicilar/profil.html', {'profil': profil})