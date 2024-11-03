#bu modelleri yönetici paneline ekleyelim

from django.contrib import admin
from .models import Profil, Arkadas, Istatistik

admin.site.register(Profil)
admin.site.register(Arkadas)
admin.site.register(Istatistik)
