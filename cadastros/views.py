from typing import List
from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Curso, Turma, Materia, Atividade, Perfil_professor, Perfil_aluno
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404  

# Create your views here.

####################### CREATE ###################


class CursoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Curso
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cursos'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context

class TurmaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Turma
    fields = ['curso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Turmas'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context

class MateriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Materia
    fields = ['nome', 'turma', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Materias'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context

class AtividadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["Administrador", "Docente"]
    model = Atividade
    fields = ['descricao', 'curso', 'materia', 'usuario', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Atividades'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context

class Perfil_professorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Perfil_professor
    fields = ['nome', 'idade', 'titulacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Perfil do Professor'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context

class Perfil_alunoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Perfil_aluno
    fields = ['nome', 'idade', 'turma']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Perfil do Aluno'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context

####################### UPDATE ###################

class AtividadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    fields = ['descricao', 'curso', 'materia', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Atividades'
        context['botao'] = 'Salvar'
        context['cor'] = 'primary'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class CursoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Curso
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar curso'
        context['botao'] = 'Salvar'
        context['cor'] = 'primary'
        return context

class TurmaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Turma
    fields = ['curso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar turma'
        context['botao'] = 'Salvar'
        context['cor'] = 'primary'
        return context

class MateriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Materia
    fields = ['nome', 'turma', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar materia'
        context['botao'] = 'Salvar'
        context['cor'] = 'primary'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Materia, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
        
class Perfil_professorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Docente"
    model = Perfil_professor
    fields = ['nome', 'idade', 'titulacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = Perfil_professor.objects.get(professor=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Perfil Professor'
        context['botao'] = 'Salvar'
        context['cor'] = 'primary'
        return context


class Perfil_alunoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Alunos"
    model = Perfil_aluno
    fields = ['nome', 'idade', 'turma']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = Perfil_aluno.objects.get(aluno=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Perfil Aluno'
        context['botao'] = 'Salvar'
        context['cor'] = 'primary'
        return context
####################### DELETE ###################

class AtividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Exlusão de Atividade'
        context['botao'] = 'Excluir'
        context['cor'] = 'danger'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
class CursoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Curso
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Exlusão de Curso'
        context['botao'] = 'Excluir'
        context['cor'] = 'danger'
        return context

class TurmaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Turma
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Exlusão da Turma'
        context['botao'] = 'Excluir'
        context['cor'] = 'danger'
        return context

class MateriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Materia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Exlusão de Materia'
        context['botao'] = 'Excluir'
        context['cor'] = 'danger'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Materia, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class Perfil_professorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Perfil_professor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Exlusão do Perfil Professor'
        context['botao'] = 'Excluir'
        context['cor'] = 'danger'
        return context
    
class Perfil_alunoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Perfil_aluno
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Exlusão do Perfil Aluno'
        context['botao'] = 'Excluir'
        context['cor'] = 'danger'
        return context


####################### LISTA ###################

class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'

    def get_queryset(self):
        self.object_list = Atividade.objects.filter(usuario=self.request.user)
        return self.object_list

class CursoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Curso
    template_name = 'cadastros/listas/curso.html'

class TurmaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Turma
    template_name = 'cadastros/listas/turma.html'

class MateriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Materia
    template_name = 'cadastros/listas/materia.html'

    def get_queryset(self):
        self.object_list = Materia.objects.filter(usuario=self.request.user)
        return self.object_list

class Perfil_professorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Perfil_professor
    template_name = 'cadastros/listas/perfil_prof.html'

class Perfil_alunoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Perfil_aluno
    template_name = 'cadastros/listas/perfil_aluno.html'
