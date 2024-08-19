# marketing/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.marketing_index, name='index'),  # Substitua 'views.index' por 'views.marketing_index'
]
