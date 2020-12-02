from django.db import models
from clases.models import Clase


class Profesores(models.Model):
    nombre = models.CharField(max_length=200)
    enseña = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    clase_impartida = models.ManyToManyField(Clase, related_name='clase_impartida')

    def __str__(self):
        return f'Nombre: {self.nombre}'