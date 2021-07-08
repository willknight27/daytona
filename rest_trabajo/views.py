from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Trabajo
from .serializers import TrabajoSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_trabajos(request):
    if request.method == 'GET':
        trabajo = Trabajo.objects.all()
        serializer = TrabajoSerializer(trabajo, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrabajoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_trabajo(request,id):

    try:
        trabajo = Trabajo.objects.get(id_trabajo=id)
    except Trabajo.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TrabajoSerializer(trabajo)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrabajoSerializer(trabajo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        trabajo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)