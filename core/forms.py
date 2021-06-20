from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Trabajo,Vehiculo


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