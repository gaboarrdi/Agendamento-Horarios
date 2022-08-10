from pyexpat import model
from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    dia = models.DateField()
    periodo = models.CharField(max_length=30)

    def __str__(self):
        return self.nome