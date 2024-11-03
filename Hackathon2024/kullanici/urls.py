#şablon görünümleri yönlendirelim.

from django.urls import path
from . import views

urlpatterns = [
    path('arkadas-ekle/<int:kullanici_id>/', views.arkadas_ekle, name='arkadas_ekle'),
    path('siralama/', views.siralama, name='siralama'),
]
