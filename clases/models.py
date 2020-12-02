from django.db import models

class Clase(models.Model):
    materia = models.CharField(max_length=200)    
    aula = models.CharField(max_length=100)    
    horas = models.IntegerField(null=True)

    def __str__(self):
        return f'Materia: {self.materia}'