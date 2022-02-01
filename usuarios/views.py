from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group

from cadastros.models import Perfil_aluno, Perfil_professor
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        # Como aqui vem os dados do forms.py, não temos o form.instance e sim o form.cleaned_data
        # pegamos o nome do grupo que o usuário marcou no select e buscamos o objeto só para garantir
        grupo = get_object_or_404(Group, name=form.cleaned_data['grupo'].name)

        # Aqui cria o usuário no banco
        url = super().form_valid(form)

        # Adiciona o grupo ao objeto usuário e salva
        self.object.groups.add(grupo)
        self.object.save()

        # Cria um perfil para este usuário
        if(grupo.name == "Alunos"):
            Perfil_aluno.objects.create(aluno=self.object)
        else:
            Perfil_professor.objects.create(professor=self.object)

        return url


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registra-se"
        context['botao'] = "Cadastrar"

        return context

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e
