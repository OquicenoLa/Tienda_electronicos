from decimal import Decimal
from bson.decimal128 import Decimal128
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from l_pedidos.forms import DetallePedidoForm, PedidoForm
from l_pedidos.models import Cliente, Pedido, PrecioProducto, Producto
from django.db.models import Sum

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")


def login_view(request):
    """Vista para mostrar el login sin autenticación"""
    try:
        pedido = Pedido.objects.first() 
        if pedido:
            return redirect('pedido_detalle', pedido_id=pedido.id)
        else:
            messages.error(request, "No hay pedidos disponibles.")
            return render(request, 'l_pedidos/login.html')
    except Pedido.DoesNotExist:
        messages.error(request, "No hay pedidos disponibles.")
        return render(request, 'l_pedidos/login.html')

def pedido_detalle(request, pedido_id):
    """Vista para mostrar el detalle de un pedido por su ID"""
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    detalles = pedido.detalles.all()  
    
    total = Decimal('0.00')
    for d in detalles:
        subtotal = d.subtotal
        if isinstance(subtotal, Decimal128):
            subtotal = subtotal.to_decimal()
        else:
            subtotal = Decimal(str(subtotal))
        total += subtotal
    
    context = {
        'pedido': pedido,
        'cliente_nombre': pedido.cliente.nombre,
        'fecha_pedido': pedido.fecha_pedido,
        'estado': pedido.estado,
        'detalles': detalles,
        'total': total  
    }
    
    return render(request, 'l_pedidos/pedido_detalle.html', context)

def crear_pedido(request):
    """Vista para crear un nuevo pedido y sus detalles"""
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        detalle_form = DetallePedidoForm(request.POST)
        
        if pedido_form.is_valid() and detalle_form.is_valid():
            
            pedido = pedido_form.save()

            detalle = detalle_form.save(commit=False)
            detalle.pedido = pedido
            detalle.save()

            return redirect('pedido_detalle', pedido_id=pedido.id)
    else:
        pedido_form = PedidoForm()
        detalle_form = DetallePedidoForm()

    return render(request, 'l_pedidos/crear_pedido.html', {
        'pedido_form': pedido_form,
        'detalle_form': detalle_form
    })

def cargar_datos_prueba(request):
    Cliente.objects.create(nombre='Carlos Pérez', email='carlos@example.com')
    Cliente.objects.create(nombre='Ana Gómez', email='ana@example.com')

    teclado = Producto.objects.create(nombre='Teclado', descripcion='Teclado mecánico RGB', stock=10)
    mouse = Producto.objects.create(nombre='Mouse', descripcion='Mouse óptico', stock=15)

    PrecioProducto.objects.create(producto=teclado, precio=Decimal('120.50'))
    PrecioProducto.objects.create(producto=mouse, precio=Decimal('59.90'))

    return HttpResponse("Datos de prueba cargados correctamente.")

def lista_pedidos(request):
    pedidos = Pedido.objects.select_related('cliente').order_by('-fecha_pedido')
    return render(request, 'l_pedidos/lista_pedidos.html', {'pedidos': pedidos})
