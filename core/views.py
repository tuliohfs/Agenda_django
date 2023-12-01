from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required(login_url='/login/')
def lista_eventos(request):
    
    user = request.user
    usuario = request.user
    # 'Evento.objects.all()' está pegando todos os objetos do modelo Evento.
    evento_instance = Evento.objects.filter(usuario=usuario)
    # 'dados' é um dicionário que contém os dados que você quer passar para o template.
    dados = {'Evento_instance': evento_instance}
    # 'render' está renderizando o template 'agenda.html' e passando o dicionário 'dados' para ele.
    return render(request, 'agenda.html', dados)

def login_user(request):
    return render(request, 'login.html')

def index(request):
    return redirect('/Agenda/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/')
    

def logout_user(request):
    logout(request)
    return redirect('/')