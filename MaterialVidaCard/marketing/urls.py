# marketing/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('campanha/<int:id>/', views.download_campanha, name='download_campanha'),
    path('material/<int:id>/', views.download_material, name='download_material'),
    path('upload/campanha/', views.upload_campanha, name='upload_campanha'),
    path('upload/material/', views.upload_material_apoio, name='upload_material_apoio'),
]
