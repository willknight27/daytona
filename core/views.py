from django.shortcuts import render
from .models import Trabajo


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