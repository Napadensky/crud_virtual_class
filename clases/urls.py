from django.urls import path
from clases.models import Clase
from clases.views import ClaseListView,ClaseDetail

urlpatterns = [
    path('', ClaseListView.as_view(),name='Clases'),
    path('<int:pk>', ClaseDetail.as_view(), name='Clase')
]