from decimal import Decimal
from django.db import models
from bson.decimal128 import Decimal128
from decimal import Decimal

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def clean(self):
        if not self.email:
            raise ValueError("El correo electrónico no puede ser vacío.")
     
    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20, 
        choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado')]
    )

    def __str__(self):  
        return f'Pedido {self.id} - {self.cliente.nombre}'


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.producto.stock >= self.cantidad:
            precio_obj = self.producto.precios.first()
            if not precio_obj:
                raise ValueError("El producto no tiene un precio asignado.")

            precio = precio_obj.precio
            if isinstance(precio, Decimal128):
                precio = precio.to_decimal()
            else:
                precio = Decimal(str(precio))

            self.subtotal = self.cantidad * precio
            self.producto.stock -= self.cantidad
            self.producto.save()

            super().save(*args, **kwargs)
        else:
            raise ValueError("No hay suficiente stock para este producto.")

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en Pedido {self.pedido.id}'
class Pago(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    metodo = models.CharField(
        max_length=20, 
        choices=[('Tarjeta', 'Tarjeta'), ('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia')]
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pago de {self.monto} para Pedido {self.pedido.id}'

class PrecioProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='precios')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Precio para {self.producto.nombre} - {self.precio}"
