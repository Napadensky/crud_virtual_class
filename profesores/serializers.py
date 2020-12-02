from rest_framework import serializers
from profesores.models import Profesores

class ProfesoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesores
        fields = ('__all__')