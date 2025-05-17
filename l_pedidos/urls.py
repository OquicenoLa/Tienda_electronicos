from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='inicio'), 
    path('pedido/<int:pedido_id>/', views.pedido_detalle, name='pedido_detalle'),
    path('crear-pedido/', views.crear_pedido, name='crear_pedido'),
    path('cargar-datos/', views.cargar_datos_prueba, name='cargar_datos'),
    path('l_pedidos/', views.lista_pedidos, name='lista_pedidos'),
]
