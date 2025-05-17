from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('editar/<int:item_id>/', views.editar_item, name='editar_item'),
    path('eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('checkout/', views.checkout, name='checkout'),
    path('aplicar_cupon/', views.aplicar_cupon, name='aplicar_cupon'),
]