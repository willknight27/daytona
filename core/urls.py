from unicodedata import name
from django.urls import path
from .views import eliminar_trabajos, home,contacto, listar_trabajos, registro,trabajos,agregar_trabajo,modificar_trabajos


urlpatterns = [
    path('', home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('trabajos/',trabajos,name="trabajos"),
    path('agregar-trabajo/',agregar_trabajo,name="agregar-trabajo"),
    path('listar-trabajos/',listar_trabajos,name="listar-trabajos"),
    path('modificar-trabajos/<id>/',modificar_trabajos,name='modificar-trabajos'),
    path('eliminar-trabajos/<id>/',eliminar_trabajos,name='eliminar-trabajos'),
    path('registro/',registro,name='registro'),

]