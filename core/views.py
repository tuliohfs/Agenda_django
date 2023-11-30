from django.shortcuts import render, redirect
from core.models import Evento

def index(request):
    return redirect('/Agenda/')


def lista_eventos(request):
    
    usuario = request.user
    # 'Evento.objects.all()' está pegando todos os objetos do modelo Evento.
    evento_instance = Evento.objects.all()
    # 'dados' é um dicionário que contém os dados que você quer passar para o template.
    dados = {'Evento_instance': evento_instance}
    # 'render' está renderizando o template 'agenda.html' e passando o dicionário 'dados' para ele.
    return render(request, 'agenda.html', dados)