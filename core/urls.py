from unicodedata import name
from django.urls import path
from .views import home,contacto,trabajos,agregar_trabajo


urlpatterns = [
    path('', home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('trabajos/',trabajos,name="trabajos"),
    path('agregar-trabajo/',agregar_trabajo,name="agregar-trabajo"),
]