from importlib.metadata import files
from django.shortcuts import render,redirect,get_object_or_404
from .models import Trabajo
from .forms import TrabajoForm,VehiculoForm,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Permisos de acceso del lado del servidor -> @permission_required('core.add_trabajo')
from django.contrib.auth.decorators import login_required,permission_required


#VISTAS

def home(request):
    return render(request,'core/index.html')

# @login_required -> solo con login puede ver
def contacto(request):
    return render(request,'core/contacto.html')

def trabajos(request):
    trabajos = Trabajo.objects.all()
    data = {
        'trabajos' : trabajos
    }
    return render(request,'core/trabajos.html',data)

@permission_required('core.add_trabajo')
def agregar_trabajo(request):

    data = {
        'form': TrabajoForm()
    }


    if request.method == 'POST':
        formulario = TrabajoForm(data = request.POST,files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Trabajo Agregado")
            return redirect(to='listar-trabajos')
        else:
            data["form"] = formulario

    return render(request,'core/lista_trabajos/agregar.html',data)

@permission_required('core.add_vehiculo')
def agregar_vehiculo(request):

    data = {
        'form': VehiculoForm()
    }


    if request.method == 'POST':
        formulario = VehiculoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Vehiculo Agregado")
            return redirect(to='home')
        else:
            data["form"] = formulario

    return render(request,'core/lista_trabajos/agregar_vehiculo.html',data)

@permission_required('core.view_trabajo')
def listar_trabajos(request):
    trabajos = Trabajo.objects.all()

    data = {
        'trabajos': trabajos
    }

    return render(request, 'core/lista_trabajos/listar.html',data)

@permission_required('core.change_trabajo')
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
   
@permission_required('core.delete_trabajo')
def eliminar_trabajos(request, id):
    
    trabajo = get_object_or_404(Trabajo, id_trabajo = id)
    trabajo.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to='listar-trabajos')

def registro(request):

    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Registro de usuario exitoso")
            return redirect(to=home)
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)
