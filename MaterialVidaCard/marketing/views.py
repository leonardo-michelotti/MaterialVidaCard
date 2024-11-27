from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .drive_service import get_drive_service


def list_files_in_folder(service, folder_id):
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields="files(id, name, webViewLink, webContentLink)").execute()
    return results.get('files', [])

@login_required
def marketing_index(request):
    service = get_drive_service()

    # IDs das pastas no Google Drive
    campanhas_folder_id = '1awW6ZIfcohpuPHIrNI5yoFblsq1f7PFr'
    material_apoio_folder_id = '1x7bGV_2bHUP0KFCs1Nk1SnJA-QaO0a08'

    # Fetching files from Google Drive folders
    campanhas = list_files_in_folder(service, campanhas_folder_id)
    materiais_apoio = list_files_in_folder(service, material_apoio_folder_id)

    # Process selected campaign
    selected_campaign_id = request.GET.get('selected_campaign')
    selected_campaign = None
    if selected_campaign_id:
        selected_campaign = next((file for file in campanhas if file['id'] == selected_campaign_id), None)

    # Process selected material of support
    selected_material_id = request.GET.get('selected_material')
    selected_material = None
    if selected_material_id:
        selected_material = next((file for file in materiais_apoio if file['id'] == selected_material_id), None)

    return render(request, 'marketing/index.html', {
        'campanhas': campanhas,
        'materiais_apoio': materiais_apoio,
        'selected_campaign': selected_campaign,
        'selected_campaign_id': selected_campaign_id,
        'selected_material': selected_material,
        'selected_material_id': selected_material_id,
    })


def test_drive_connection(request):
    service = get_drive_service()
    about = service.about().get(fields="user").execute()
    return HttpResponse(f"Connected to Google Drive as {about['user']['emailAddress']}")
