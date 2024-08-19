# marketing/views.py

from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .drive_service import get_drive_service


def list_files_in_folder(service, folder_id):
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields="files(id, name, webViewLink, webContentLink)").execute()
    return results.get('files', [])


def marketing_index(request):
    service = get_drive_service()

    # IDs das pastas no Google Drive
    campanhas_folder_id = '1awW6ZIfcohpuPHIrNI5yoFblsq1f7PFr'
    material_apoio_folder_id = '1x7bGV_2bHUP0KFCs1Nk1SnJA-QaO0a08'

    campanhas = list_files_in_folder(service, campanhas_folder_id)
    materiais_apoio = list_files_in_folder(service, material_apoio_folder_id)

    return render(request, 'marketing/index.html', {
        'campanhas': campanhas,
        'materiais_apoio': materiais_apoio,
    })


def test_drive_connection(request):
    service = get_drive_service()
    about = service.about().get(fields="user").execute()
    return HttpResponse(f"Connected to Google Drive as {about['user']['emailAddress']}")