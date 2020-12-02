from rest_framework import serializers
from estudiantes.models import Estudiante

class EstudianteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('__all__')