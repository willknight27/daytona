from django.urls import path
from .views import home,contacto,trabajos


urlpatterns = [
    path('', home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('trabajos/',trabajos,name="trabajos"),
    
]