from django.urls import path
from rest_trabajo.views import lista_trabajos,detalle_trabajo

urlpatterns = [
    path('lista-trabajos',lista_trabajos,name='lista-trabajos'),
    path('detalle-trabajo/<id>',detalle_trabajo, name = 'detalle-trabajo'),
]
