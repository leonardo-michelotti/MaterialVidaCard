# accounts/views.py

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # Adicione esta linha
from django.shortcuts import redirect, render

from .forms import EmailLoginForm
from .models import AuthorizedEmail


def login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if AuthorizedEmail.objects.filter(email=email, is_active=True).exists():
                # Cria ou obtem o usuário
                user, created = User.objects.get_or_create(username=email, email=email)
                user = authenticate(request, username=email)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.error(request, 'Falha na autenticação.')
            else:
                messages.error(request, 'Email não autorizado.')
        else:
            messages.error(request, 'Formulário inválido.')
    else:
        form = EmailLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
