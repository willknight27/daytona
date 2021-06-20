from django.shortcuts import render
from .models import Trabajo
from .forms import TrabajoForm

#VISTAS

def home(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request,'core/contacto.html')

def trabajos(request):
    trabajos = Trabajo.objects.all()
    data = {
        'trabajos' : trabajos
    }
    return render(request,'core/trabajos.html',data)

def agregar_trabajo(request):

    data = {
        'form': TrabajoForm()
    }

    return render(request,'core/lista_trabajos/agregar.html',data)
