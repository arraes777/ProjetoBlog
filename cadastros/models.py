from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Curso(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
     return self.nome


class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        return self.curso.nome


class Materia(models.Model):
    nome = models.CharField(max_length=50)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)

    def __str__(self):
     return self.nome

class Atividade(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    data_postagem = models.DateTimeField(verbose_name="Data da postagem", auto_now_add=True)
    arquivo = models.FileField(upload_to='pdf/')

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.descricao, self.data_postagem)


class Perfil_professor(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Nome Completo", null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    idade = models.IntegerField(null=True)
    titulacao = models.CharField(max_length=100, verbose_name="Titulação", null=True)

    professor = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.nome_completo, self.cpf, self.idade, self.titulacao)


class Perfil_aluno(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Nome Completo", null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    idade = models.IntegerField(null=True)

    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, null=True)
    aluno = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return "{} ({})".format(self.nome_completo, self.cpf, self.turma, self.idade)
