from django.urls import path
from rest_trabajo.views import lista_trabajos

urlpatterns = [
    path('lista-trabajos',lista_trabajos,name='lista-trabajos'),
]
