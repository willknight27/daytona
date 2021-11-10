from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Trabajo,Vehiculo
from django.contrib.auth.forms import UserCreationForm
#importar modelo de usuario
from django.contrib.auth.models import User


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = '__all__'

        widgets = {

            "fecha" : forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    #pass
    class Meta:

        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]


