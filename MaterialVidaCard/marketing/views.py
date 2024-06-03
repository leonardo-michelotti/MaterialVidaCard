# marketing/views.py

from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CampanhaForm, MaterialApoioForm
from .models import Campanha, MaterialApoio


@login_required
def index(request):
    campanhas = Campanha.objects.all()
    materiais = MaterialApoio.objects.all()
    return render(request, 'marketing/index.html', {'campanhas': campanhas, 'materiais': materiais})

@login_required
def download_campanha(request, id):
    campanha = get_object_or_404(Campanha, id=id)
    return FileResponse(campanha.arquivo.open(), as_attachment=True)

@login_required
def download_material(request, id):
    material = get_object_or_404(MaterialApoio, id=id)
    return FileResponse(material.arquivo.open(), as_attachment=True)

@login_required
def upload_campanha(request):
    if request.method == 'POST':
        form = CampanhaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CampanhaForm()
    return render(request, 'marketing/upload_campanha.html', {'form': form})

@login_required
def upload_material_apoio(request):
    if request.method == 'POST':
        form = MaterialApoioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MaterialApoioForm()
    return render(request, 'marketing/upload_material_apoio.html', {'form': form})
