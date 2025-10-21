from django.shortcuts import get_object_or_404, redirect, render
from projects.models import Projeto
from .models import Tarefa

def detalhe_tarefa(request, tarefa_id):

    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)

    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})

from django.shortcuts import render
from .models import Tarefa
from django.http import HttpResponse
def listar_tarefas(request):
    tarefas_salvas=Tarefa.objects.all()
    contexto={"minhas_tarefas":tarefas_salvas}
    return render (request,'tarefas/lista.html',contexto)