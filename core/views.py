from django.shortcuts import render
from .models import Trabajo
from .forms import TrabajoForm,VehiculoForm

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
        'form': TrabajoForm(),
        'form_vehiculo': VehiculoForm(),
    }



    if request.method == 'POST':
        formulario = TrabajoForm(data = request.POST,files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado exitoso"
        else:
            data["form"] = formulario
    


    if request.method == 'POST':
        formulario_vehiculo = VehiculoForm(data = request.POST)
        if formulario_vehiculo.is_valid():
            formulario_vehiculo.save()
            data["mensaje"] = "guardado exitoso"
        else:
            data["from_vehiculo"] = formulario_vehiculo

    return render(request,'core/lista_trabajos/agregar.html',data)


def listar_trabajos(request):
    trabajos = Trabajo.objects.all()

    data = {
        'trabajos': trabajos
    }

    return render(request, 'core/lista_trabajos/listar.html',data)

