from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, ItemCarrito, Pedido, ItemPedido, Cupon
from django.contrib import messages

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'carro_compras/lista_productos.html', {'productos': productos})

def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario_id=request.session.session_key)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'carro_compras/carrito.html', {'items': items, 'total': total})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario_id=request.session.session_key)
    item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not item_creado:
        item.cantidad += 1
        item.save()
    return redirect('lista_productos')

def editar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, pk=item_id)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad'))
        if cantidad > 0:
            item.cantidad = cantidad
            item.save()
        return redirect('ver_carrito')
    return render(request, 'carro_compras/editar_item.html', {'item': item})

def eliminar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, pk=item_id)
    item.delete()
    return redirect('ver_carrito')

def lista_pedidos(request):
    pedidos = Pedido.objects.filter(usuario_id=request.session.session_key)
    return render(request, 'carro_compras/lista_pedidos.html', {'pedidos': pedidos})

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    items = ItemPedido.objects.filter(pedido=pedido)
    return render(request, 'carro_compras/detalle_pedido.html', {'pedido': pedido, 'items': items})

def checkout(request):
    carrito = get_object_or_404(Carrito, usuario_id=request.session.session_key)
    items = ItemCarrito.objects.filter(carrito=carrito)
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        pedido = Pedido.objects.create(
            usuario_id=request.session.session_key,
            total=sum(item.producto.precio * item.cantidad for item in items),
            estado='Pendiente',
            direccion_envio=direccion
        )
        for item in items:
            ItemPedido.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                precio=item.producto.precio
            )
        carrito.delete()
        return render(request, 'carro_compras/confirmacion_pedido.html', {'pedido': pedido})
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'carro_compras/checkout.html', {'items': items, 'total': total})

def aplicar_cupon(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        try:
            cupon = Cupon.objects.get(codigo=codigo)
            request.session['descuento'] = float(cupon.descuento)
            messages.success(request, 'Cupón aplicado correctamente')
        except Cupon.DoesNotExist:
            messages.error(request, 'Cupón no válido')
    return redirect('ver_carrito')