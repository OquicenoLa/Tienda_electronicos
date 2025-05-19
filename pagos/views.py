from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ShippingForm
from .models import Payment, PaymentMethod
from carro_compras.models import Carrito, ItemCarrito

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

def shipping_view(request):
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            # Obtener el session_key, si no existe, crearlo
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            try:
                carrito = Carrito.objects.get(usuario_id=session_key)
            except Carrito.DoesNotExist:
                return HttpResponse("No hay carrito de compras activo para este usuario.")
            items = ItemCarrito.objects.filter(carrito=carrito)
            if not items.exists():
                return HttpResponse("El carrito está vacío.")
            total = sum(item.producto.precio * item.cantidad for item in items)

            if not request.user.is_authenticated:
                return HttpResponse("Debes iniciar sesión para continuar con el pago.")

            payment = Payment.objects.create(
                user=request.user,
                total=total,
                status='pending'
            )

            # Aquí podrías guardar los datos de envío/facturación si lo deseas
            # Por ejemplo: payment.shipping_name = form.cleaned_data['name']
            # payment.save()

            return redirect('confirmacion_pago', payment_id=payment.id)
    else:
        form = ShippingForm()

    return render(request, 'pagos/shipping_form.html', {'form': form, 'ocultar_facturacion': False})

def confirmacion_pago(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    return render(request, 'pagos/confirmacion.html', {'payment': payment})