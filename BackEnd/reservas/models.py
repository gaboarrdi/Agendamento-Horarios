from django.db import models

# Create your models here.
class Reserva(models.Model):
    nome = models.CharField(max_length=30)
    dia = models.DateField()
    periodo = models.CharField(max_length=30)
    mesa = models.CharField(max_length=30)

    def __str__(self):
        return self.nome