from django.shortcuts import render
from rest_framework import serializers, viewsets
from core.models import Trabajo
from .serializers import TrabajoSerializer

class TrabajoAPI(viewsets.ModelViewSet):
    queryset = Trabajo.objects.all()
    serializer_class = TrabajoSerializer