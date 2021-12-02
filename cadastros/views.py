from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Curso, Turma, Materia, Atividade, Perfil_professor, Perfil_aluno
from django.urls import reverse_lazy

# Create your views here.
class CursoCreate(CreateView):
    model = Curso
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class TurmaCreate(CreateView):
    model = Turma
    fields = ['curso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class MateriaCreate(CreateView):
    model = Materia
    fields = ['nome', 'turma']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['descricao', 'curso', 'materia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class Perfil_professorCreate(CreateView):
    model = Perfil_professor
    fields = ['nome', 'idade', 'titulacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class Perfil_alunoCreate(CreateView):
    model = Perfil_aluno
    fields = ['nome', 'idade', 'turma']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


