from django.contrib import admin
from ControleEscola.models import *

# Register your models here.

class AlunosAdmin(admin.ModelAdmin):
    list_display = ['id_aluno', 'nome', 'data_nascimento', 'sexo', 'data_cadastro', 'login_cadastro']
    search_fields = ['id_aluno', 'nome', 'login_cadastro']
    list_filter = ['sexo', 'data_cadastro', 'data_nascimento']

class CursosAdmin(admin.ModelAdmin):
    list_display = ['id_curso', 'nome_curso', 'data_cadastro', 'login_cadastro']
    search_fields = ['id_curso', 'nome_curso', 'login_cadastro']
    list_filter = ['data_cadastro']

class TurmasAdmin(admin.ModelAdmin):
    list_display = ['id_turma', 'id_curso', 'data_inicio', 'data_termino', 'data_cadastro', 'login_cadastro']
    search_fields = ['id_turma', 'id_curso',  'login_cadastro']
    list_filter = ['data_inicio', 'data_termino', 'data_cadastro',]

class SituacaoAdmin(admin.ModelAdmin):
    list_display = ['id_situacao', 'situacao', 'data_cadastro', 'login_cadastro']
    search_fields = ['id_situacao', 'login_cadastro']
    list_filter = ['situacao', 'data_cadastro']

class ATAdmin(admin.ModelAdmin):
    list_display = ['id','id_turma', 'aluno', 'valor', 'valor_desconto', 'data_cadastro', 'login_cadastro']
    search_fields = ['id', 'login_cadastro']
    list_filter = ['valor','valor_desconto','data_cadastro']

class PresencaAdmin(admin.ModelAdmin):
    list_display = ['id_turma', 'aluno', 'situacao', 'data_presenca', 'data_cadastro', 'login_cadastro']
    search_fields = ['login_cadastro']
    list_filter = ['situacao', 'data_presenca', 'data_cadastro']

admin.site.register(Alunos, AlunosAdmin)
admin.site.register(Cursos, CursosAdmin) 
admin.site.register(Turmas, TurmasAdmin)
admin.site.register(Situacao, SituacaoAdmin)
admin.site.register(Alunosxturmas, ATAdmin) 
admin.site.register(Presenca, PresencaAdmin)