from django.contrib import admin
from .models import Categoria,Trabajo,Mecanico,Vehiculo

# REGISTRAR MODELOS

admin.site.register(Categoria)
admin.site.register(Mecanico)
admin.site.register(Vehiculo)
admin.site.register(Trabajo)
