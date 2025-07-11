from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm

@login_required(login_url='login')
def home(request):
    templates = 'spotify/home.html'
    context = {
        'user': request.user,
    }
    return render(request,templates,context)

def login_view(request):
    templates = 'spotify/login.html'
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo de volta, {username}!")
                # Redireciona para a URL definida em settings.LOGIN_REDIRECT_URL
                return redirect('home') # Ou o nome da sua view principal
            else:
                messages.error(request, "Nome de usuário ou senha inválidos.")
        else:
            # Erros do formulário (ex: campos vazios)
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = LoginForm()
    
    return render(request, templates, {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Você foi desconectado com sucesso.")
    return redirect('login')
