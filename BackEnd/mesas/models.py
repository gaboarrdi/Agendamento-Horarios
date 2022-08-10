from django.db import models

# Create your models here.
class Mesa(models.Model):
    numero = models.CharField(max_length=2)
    

    def __str__(self):
        return self.numero