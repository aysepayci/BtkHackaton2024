#basit bir arkadaş ekleme ve kullanıcı sıralaması işlevi ekleyelim.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profil, Arkadas, Istatistik

def arkadas_ekle(request, kullanici_id):
    kullanici = User.objects.get(id=kullanici_id)
    Arkadas.objects.create(kullanici=request.user, arkadas=kullanici)
    return redirect('profil', kullanici_id=kullanici_id)

def siralama(request):
    profiller = Profil.objects.all().order_by('-puan')
    return render(request, 'kullanici/siralama.html', {'profiller': profiller})
