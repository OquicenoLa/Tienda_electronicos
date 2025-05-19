from django import forms

class ShippingForm(forms.Form):
    #Campos de envío
    name = forms.CharField(max_length=50, label='Primer nombre')
    last_name = forms.CharField(max_length=50, label='Apellido')
    address = forms.CharField(max_length=255, label='Dirección')
    complements = forms.CharField(max_length=255, required=False, label='Apt, casa o datos adicionales.')
    zip_code = forms.CharField(max_length=20, label='Código postal')
    city = forms.CharField(max_length=50, label='Ciudad')
    departamentos = forms.CharField(label='Departamento')
    pais = forms.CharField(label='País')
    phone_code = forms.CharField(max_length=5, label='Código de área')
    phone_number = forms.CharField(max_length=20, label='Número de celular')

    ocultar_facturacion = forms.BooleanField(required=False, label='Misma información de facturación')
    
    #Campos de facturación
    nombre_facturacion = forms.CharField(max_length=50, required=False, label='Nombre de facturación')
    apellido_facturacion = forms.CharField(max_length=50, required=False, label='Apellido de facturación')
    direccion_facturacion = forms.CharField(max_length=255, required=False, label='Dirección de facturación')
    complemento_facturacion = forms.CharField(max_length=255, required=False, label='Apt, casa o datos adicionales (facturación).')
    codigo_postal_facturacion = forms.CharField(max_length=20, required=False, label='Código postal (facturación)')
    ciudad_facturacion = forms.CharField(max_length=50, required=False, label='Ciudad (facturación)')
    departamento_facturacion = forms.CharField(required=False, label='Departamento (facturación)')
    pais_facturacion = forms.CharField(required=False, label='País (facturación)')
    codigo_area_facturacion = forms.CharField(max_length=5, required=False, label='Código de área (facturación)')
    telefono_facturacion = forms.CharField(max_length=20, required=False, label='Número de teléfono (facturación)')