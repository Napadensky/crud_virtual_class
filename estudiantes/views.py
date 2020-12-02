from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,status
from estudiantes.models import Estudiante
from estudiantes.serializers import EstudianteSerializers


class EstudianteListView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializers


class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializers