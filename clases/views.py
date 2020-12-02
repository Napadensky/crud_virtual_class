from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,status
from clases.models import Clase
from clases.serializers import ClaseSerializers


class ClaseListView(generics.ListCreateAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializers


class ClaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializers
