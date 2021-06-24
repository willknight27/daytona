from importlib.metadata import files
from django.shortcuts import render,redirect,get_object_or_404
from .models import Trabajo
from .forms import TrabajoForm,VehiculoForm
from django.contrib import messages

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

def modificar_trabajos(request, id):

    trabajo = get_object_or_404(Trabajo, id_trabajo = id )

    data = {
        'form': TrabajoForm(instance=trabajo)

    }

    if request.method == 'POST':
        formulario = TrabajoForm(data=request.POST, instance=trabajo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to='listar-trabajos')
        data["form"] = formulario

    return render(request, 'core/lista_trabajos/modificar.html',data)
   

def eliminar_trabajos(request, id):
    
    trabajo = get_object_or_404(Trabajo, id_trabajo = id)
    trabajo.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to='listar-trabajos')