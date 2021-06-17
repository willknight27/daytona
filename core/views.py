from django.shortcuts import render

#VISTAS

def home(request):
    return render(request,'core/index.html')


