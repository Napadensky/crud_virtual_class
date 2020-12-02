from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,status
from profesores.models import Profesores
from profesores.serializers import ProfesoresSerializers


class ProfesoresListView(generics.ListCreateAPIView):
    queryset = Profesores.objects.all()
    serializer_class = ProfesoresSerializers


class ProfesoresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesores.objects.all()
    serializer_class = ProfesoresSerializers