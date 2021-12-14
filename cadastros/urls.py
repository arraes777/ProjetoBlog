from os import name
from django.urls import path
from .views import *


urlpatterns = [
    # Criar todos os endereços/rotas
############## ATIVIDADE ##############
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(),name='editar-atividade'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('listar/atividade/', AtividadeList.as_view(), name='listar-atividade'),

############## CURSO ##############
    path('cadastrar/curso/', CursoCreate.as_view(), name='cadastrar-curso'),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(),name='editar-curso'),
    path('excluir/curso/<int:pk>/', CursoDelete.as_view(), name='excluir-curso'),
    path('listar/curso/', CursoList.as_view(), name='listar-curso'),

############## Turma ##############
    path('cadastrar/turma/', TurmaCreate.as_view(), name='cadastrar-turma'),
    path('editar/turma/<int:pk>/', TurmaUpdate.as_view(), name='editar-turma'),
    path('excluir/turma/<int:pk>/', TurmaDelete.as_view(), name='excluir-turma'),
    path('listar/turma/', TurmaList.as_view(), name='listar-turma'),

############## Materia ##############
    path('cadastrar/materia/', MateriaCreate.as_view(), name='cadastrar-materia'),
    path('editar/materia/<int:pk>/', MateriaUpdate.as_view(), name='editar-materia'),
    path('excluir/materia/<int:pk>/', MateriaDelete.as_view(), name='excluir-materia'),
    path('listar/materia/', MateriaList.as_view(), name='listar-materia'),

############## Perfil Professor ##############
    path('cadastrar/perfil_prof/', Perfil_professorCreate.as_view(), name='cadastrar-perfil_prof'),
    path('editar/perfil_prof/<int:pk>/', Perfil_professorUpdate.as_view(), name='editar-perfil_prof'),
    path('excluir/perfil_prof/<int:pk>/', Perfil_professorDelete.as_view(), name='excluir-perfil_prof'),
    path('listar/perfil_prof/', Perfil_professorList.as_view(), name='listar-perfil_prof'),

############## Perfil Aluno ##############
    path('cadastrar/perfil_aluno/', Perfil_alunoCreate.as_view(), name='cadastrar-perfil_aluno'),
    path('editar/perfil_aluno/<int:pk>/', Perfil_alunoUpdate.as_view(), name='editar-perfil_aluno'),
    path('excluir/perfil_aluno/<int:pk>/', Perfil_alunoDelete.as_view(), name='excluir-perfil_aluno'),
    path('listar/perfil_aluno/', Perfil_alunoList.as_view(), name='listar-perfil_aluno'),

]
