# marketing/forms.py

from django import forms

from .models import Campanha, MaterialApoio


class CampanhaForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim', 'arquivo']

class MaterialApoioForm(forms.ModelForm):
    class Meta:
        model = MaterialApoio
        fields = ['nome', 'descricao', 'arquivo']
