from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombrep = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombrep

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    creada_en = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    
class EspecificacionTecnica(models.Model):
    clave = models.CharField(max_length=100)
    valor = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.clave}: {self.valor}"
    
    
# Create your models here.
