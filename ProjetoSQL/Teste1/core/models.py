from django.db import models

# Create your models here.
class Cursos(models.Model):
    id_curso = models.DecimalField(db_column='ID_CURSO', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
    nome_curso = models.CharField(db_column='NOME_CURSO', max_length=200)  # Field name made lowercase.
    data_cadastro = models.DateField(db_column='DATA_CADASTRO')  # Field name made lowercase.
    login_cadastro = models.CharField(db_column='LOGIN_CADASTRO', max_length=15)  # Field name made lowercase.
    data_alteracao = models.DateField(db_column='DATA_ALTERACAO', blank=True, null=True)  # Field name made lowercase.
    login_alteracao = models.CharField(db_column='LOGIN_ALTERACAO', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cursos'
        ordering = ['id_curso']
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome_curso 

