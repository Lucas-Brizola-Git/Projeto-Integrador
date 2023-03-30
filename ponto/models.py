from django.db import models
from datetime import date
from usuarios.models import Usuario

class Pontos(models.Model):
    #userId = models.
    chekin = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Ponto'
    #def __str__(self):
    #    return self.date
