from os import name
from django.urls import path
from .views import *

from .views import AtividadeCreate, AtividadeUpdate, AtividadeDelete, AtividadeList

urlpatterns = [
    # Criar todos os endereços/rotas
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(),name='editar-atividade'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('listar/atividade/', AtividadeList.as_view(), name='listar-atividade')

]
