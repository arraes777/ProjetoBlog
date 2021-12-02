from django.contrib import admin

from .models import Curso, Turma, Materia, Atividade, Perfil_professor, Perfil_aluno
# Register your models here.

admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Materia)
admin.site.register(Atividade)
admin.site.register(Perfil_professor)
admin.site.register(Perfil_aluno)



