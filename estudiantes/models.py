from django.db import models
from clases.models import Clase

class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)
    activo = models.BooleanField(default=True)

    clase = models.ManyToManyField(Clase, related_name='clases')

    def __str__(self):
        return f'Nombre: {self.nombre}'