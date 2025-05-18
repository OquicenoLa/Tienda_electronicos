from django.urls import path
from .views import *

urlpatterns = [
##    path('', home, name='home'),  # Vista de la página principal (ajustar si es otra vista)
    path('home/', home, name='home'),  # Vista de la página principal (ajustar si es otra vista)   
]