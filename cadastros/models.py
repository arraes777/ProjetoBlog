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

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.descricao, self.data_postagem)


class Perfil_professor(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    titulacao = models.CharField(max_length=100, verbose_name="Titulação")

    def __str__(self):
        return "{} ({})".format(self.nome, self.idade, self.titulacao)


class Perfil_aluno(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()

    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome, self.turma, self.idade)
