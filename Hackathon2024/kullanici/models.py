#kullanıcı profili, arkadaş ekleme ve istatistiklerin kaydedilmesi için gerekli modelleri ekleyelim.

from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    puan = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class Arkadas(models.Model):
    kullanici = models.ForeignKey(User, related_name="arkadaslar", on_delete=models.CASCADE)
    arkadas = models.ForeignKey(User, related_name="arkadas_olunanlar", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kullanici} -> {self.arkadas}"

class Istatistik(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    tamamlanan_gorevler = models.IntegerField(default=0)
    harcanan_zaman = models.IntegerField(default=0)  # dakika olarak
    basari_orani = models.FloatField(default=0.0)
    tarih = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.kullanici.username} - {self.tarih}"
