from django.urls import path
from profesores.models import Profesores
from profesores.views import ProfesoresListView,ProfesoresDetail

urlpatterns = [
    path('', ProfesoresListView.as_view(),name='Profesores'),
    path('<int:pk>', ProfesoresDetail.as_view(), name='Profesor')
]