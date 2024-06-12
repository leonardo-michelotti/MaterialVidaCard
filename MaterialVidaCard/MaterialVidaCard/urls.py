from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketing/', include('marketing.urls')),
    path('accounts/', include('accounts.urls')),
    path('', lambda request: redirect('login', permanent=False)),  # Redireciona a raiz para a página de login
]
