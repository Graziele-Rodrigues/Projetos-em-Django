from django.db import models

# Create your models here.
class Alunos(models.Model):
    id_aluno = models.IntegerField(primary_key=True, db_column='id_aluno')
    nome = models.CharField(max_length=200, db_column='nome')
    data_nascimento = models.DateField(db_column='data_nascimento')
    sexo = models.CharField(max_length=1, db_column='sexo')
    data_cadastro = models.DateTimeField(db_column='data_cadastro')
    login_cadastro = models.CharField(max_length=15, db_column='login_cadastro')

    class Meta:
        managed = False
        db_table = 'ALUNOS'
        ordering = ['id_aluno']
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome


class Cursos(models.Model):
    id_curso = models.IntegerField(primary_key=True, db_column='id_curso')
    nome_curso = models.CharField(max_length=200, db_column='nome_curso')
    data_cadastro = models.DateTimeField(db_column='data_cadastro')
    login_cadastro = models.CharField(max_length=15,db_column='login_cadastro')

    class Meta:
        managed = False
        db_table = 'CURSOS'
        ordering = ['id_curso']
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome_curso 


class Turmas(models.Model):
    id_turma = models.IntegerField(primary_key=True, db_column='id_turma')
    id_curso = models.IntegerField(db_column='id_curso')
    data_inicio = models.DateField(db_column='data_inicio')
    data_termino = models.DateField(blank=True, null=True, db_column='data_termino')
    data_cadastro = models.DateTimeField(db_column='data_cadastro')
    login_cadastro = models.CharField(max_length=15, blank=True, null=True,db_column='login_cadastro')

    class Meta:
        managed = False
        db_table = 'TURMAS'
        ordering = ['id_turma']
        verbose_name_plural = 'Turmas'

    def __str__(self):
        id = str(self.id_turma)
        return id

class Situacao(models.Model):
    id_situacao = models.IntegerField(primary_key=True, db_column='id_situacao')
    situacao = models.CharField(max_length=25,db_column='situacao')
    data_cadastro = models.DateTimeField(blank=True, null=True, db_column='data_cadastro')
    login_cadastro = models.CharField(max_length=15, blank=True, null=True, db_column='login_cadastro')

    class Meta:
        managed = False
        db_table = 'SITUACAO'
        ordering = ['data_cadastro']
        verbose_name_plural = 'Situações'

    def __str__(self):
        return self.situacao


class Alunosxturmas(models.Model):
    id = models.IntegerField(primary_key=True)
    id_turma = models.ForeignKey(Turmas, on_delete=models.DO_NOTHING, db_column='id_turma') 
    aluno = models.ForeignKey(Alunos, on_delete=models.DO_NOTHING, db_column='id_aluno') 
    valor = models.DecimalField(max_digits=13, decimal_places=2, db_column='valor')
    valor_desconto = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, db_column='valor_desconto')
    data_cadastro = models.DateTimeField(db_column='data_cadastro')
    login_cadastro = models.CharField(max_length=15, db_column='login_cadastro')
    

    class Meta:
        managed = False
        db_table = 'ALUNOSxTURMAS'
        ordering = ['id']
        verbose_name_plural = 'AlunosxTurmas'

    def __str__(self):
        id_int = str(self.id)
        return id_int


class Presenca(models.Model):
    id_turma = models.ForeignKey(Turmas, on_delete=models.DO_NOTHING, db_column='id_turma')
    aluno = models.ForeignKey(Alunos, on_delete=models.DO_NOTHING, db_column='id_aluno')
    situacao = models.ForeignKey(Situacao, on_delete=models.DO_NOTHING, db_column='id_situacao')
    data_presenca = models.DateField(primary_key=True, db_column='data_presenca')
    data_cadastro = models.DateField(db_column='data_cadastro')
    login_cadastro = models.CharField(max_length=15, db_column='login_cadastro')

    class Meta:
        managed = False
        db_table = 'PRESENCA'
        ordering = ['data_cadastro']
        verbose_name_plural = 'Presenças'

    def __str__(self):
        id = str(self.id_turma)
        return id