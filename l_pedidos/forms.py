from django import forms
from .models import Pedido, DetallePedido
from bson.decimal128 import Decimal128
from decimal import Decimal

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado']


class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad']

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')

        if not producto or not cantidad:
            raise forms.ValidationError("Producto y cantidad son obligatorios.")

        precio_obj = producto.precios.first()
        if not precio_obj:
            raise forms.ValidationError("No se encontró un precio válido para el producto.")

        valor = precio_obj.precio
        if not isinstance(valor, (Decimal, Decimal128)):
            raise forms.ValidationError("El precio del producto no es válido.")

        return cleaned_data
