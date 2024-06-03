# MaterialVidaCard/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketing/', include('marketing.urls')),
    path('accounts/', include('accounts.urls')),
]
