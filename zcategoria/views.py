from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Categoria, Marca, EspecificacionTecnica

def home(request):
    return HttpResponse('HOLA MUNDO')

def homeHTML(request):
    return HttpResponse('HOLA MUNDO CRUEL')

def index(request):
    cat1 = Categoria.objects.create(
        nombrep='Computadores',
        descripcion='Laptops, PC de escritorio y todo lo relacionado',
    )
    
    cat2 = Categoria.objects.create(
        nombrep='Tablets',
        descripcion='Tablets Android, iPads y más'
    )
    
    mar1 = Marca.objects.create(
        nombre='HP',
        pais_origen='EEUU'
    )
    
    mar2 = Marca.objects.create(
        nombre='ASUS',
        pais_origen='COL'
    )

    esp1 = EspecificacionTecnica.objects.create(
        clave='Procesador',
        valor='Intel Core i7 12ª Gen'
    )

    return render(request, 'index.html', { 
         'producto': [cat1, cat2],
        'marca': [mar1,mar2],
        'especificación': esp1, })
    
def detalle_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    marcas = Marca.objects.all()  
    especificacion = EspecificacionTecnica.objects.first()

    return render(request, 'index.html', {
        'producto': [categoria], 
        'marca': marcas,              
        'especificación': especificacion,
    })