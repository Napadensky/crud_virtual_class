from django.urls import path
from estudiantes.models import Estudiante
from estudiantes.views import EstudianteListView,EstudianteDetail

urlpatterns = [
    path('', EstudianteListView.as_view(),name='Estudiantes'),
    path('<int:pk>', EstudianteDetail.as_view(), name='Estudiantes')
]