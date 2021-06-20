from dataclasses import fields
from django import forms
from .models import Trabajo


class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = '__all__'