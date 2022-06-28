from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return redirect('/')

@login_required(login_url='login/')
def lista_eventos(request):
    usuario = request.user
    print(usuario)
    my_events = Evento.objects.filter(usuario=usuario)
    print(my_events)

    all_events = Evento.objects.all()

    print(all_events)
    dados = {'all_events': all_events, 'my_events': my_events}
    print(dados)

    return render(request, 'agenda.html', dados)
