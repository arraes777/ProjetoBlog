from os import name
from django.urls import path
from .views import *

from .views import AtividadeCreate

urlpatterns = [
    # Criar todos os endereços/rotas
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade')

]
