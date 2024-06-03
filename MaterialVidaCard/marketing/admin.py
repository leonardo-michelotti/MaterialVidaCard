# marketing/admin.py

from django.contrib import admin

from .models import Campanha, MaterialApoio

admin.site.register(Campanha)
admin.site.register(MaterialApoio)
