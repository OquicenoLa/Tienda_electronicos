"""
URL configuration for Tienda_Electronicos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pagos import views as pagos_views
from l_pedidos import views as pedidos_views
from zcategoria import views as zcagetoria_views
from carro_compras import views as carro_compras_views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('carro_compras.urls')),
    path('carro_compras/', include('carro_compras.urls')),  # Rutas de la app 'carro_compras'
    path('pedidos/', include('l_pedidos.urls')),  # Rutas de la app 'l_pedidos'
    path('pagos/', include('pagos.urls')),  # Rutas de la app 'pagos'
    path('catalogo/', include('zcategoria.urls')),  # Rutas de la app 'pagos'
    path('', home_views.home),  # Vista de la página principal (ajustar si es otra vista)
    
]
