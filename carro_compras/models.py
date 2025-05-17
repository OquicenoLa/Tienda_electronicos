from djongo import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    stock = models.IntegerField()
    descripcion = models.TextField()

    class Meta:
        db_table = 'productos'

class Carrito(models.Model):
    usuario_id = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'carritos'

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'items_carrito'

class Pedido(models.Model):
    usuario_id = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)
    direccion_envio = models.TextField()

    class Meta:
        db_table = 'pedidos'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'items_pedido'

class Cupon(models.Model):
    codigo = models.CharField(max_length=20)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    valido_hasta = models.DateField()
    usos_maximos = models.IntegerField()

    class Meta:
        db_table = 'cupones'