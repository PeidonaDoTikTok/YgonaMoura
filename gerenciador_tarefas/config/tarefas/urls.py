#DETALHES DA TAREFA
#<int:tarefa_id>- captura um numero da URL
path('<int:tarefa_id>/', views.detalhe_tarefa, name='detalhe_tarefa'),


from django.urls import path
from . import views
urlpatterns=[path('',views.listar_tarefas,name='listar_tarefas'),]