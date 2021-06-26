from distutils.command.upload import upload
from django.db import models

# MODELOS

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria


class Mecanico(models.Model):
    id_mecanico = models.IntegerField(primary_key=True)
    nombre_mecanico = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_mecanico

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)

    def __str__(self):
        return self.patente


class Trabajo(models.Model):
    id_trabajo = models.AutoField(primary_key=True)
    diagnostico = models.CharField(max_length=100)
    valor = models.IntegerField()
    fecha = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete = models.PROTECT)
    mecanico = models.ForeignKey(Mecanico, on_delete = models.PROTECT)
    vehiculo = models.ForeignKey(Vehiculo, on_delete = models.PROTECT)
    imagen = models.ImageField(upload_to="trabajos",null=True)

    def __str__(self):
        return self.diagnostico

