from pessoas.models import Pessoa
from enderecos.models import Endereco
from django.db import models

# Create your models here.
class Diligencia(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_realizacao = models.DateField(null=False, blank=False)
    mandado = models.FileField(upload_to='mandados/', null=True, blank=True)
    relatorio = models.FileField(upload_to='relatorios/', null=True, blank=True)
    dinheiro_apreendido = models.DecimalField(max_digits=15, decimal_places=2)
    obs = models.TextField()
    endereco = models.ForeignKey(Endereco, blank=False, null=False, on_delete=models.CASCADE)
    pessoa = models.ManyToManyField(Pessoa, blank=True)

    class Meta:
        verbose_name = "DiligĂȘncia"
        verbose_name_plural = "DiligĂȘncias"
        
    def __str__(self):
        return self.nome