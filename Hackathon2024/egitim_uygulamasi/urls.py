#uygulama URL’lerini ana projeye ekleyin

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kullanici/', include('kullanici.urls')),
]
