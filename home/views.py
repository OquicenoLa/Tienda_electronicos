from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    data = { 'usuario': 'Usuario', 'titulo': 'Bienvenido a la Tienda Electrónica' }
    return render(request, 'home/home.html', data)  # Asegúrate de que la plantilla 'home.html' exista en la carpeta de plantillas de tu aplicación




# Create your views here.
