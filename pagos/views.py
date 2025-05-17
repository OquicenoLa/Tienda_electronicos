from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola")

def goIndex(request):
    data = {'usuario': 'Usuario'}
    return render(request, 'Pagos en linea.html', data)

def goPagos1(request):
    return render(request, 'Pagos 1.html')

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")