from django.urls import path
from .views import goIndex, inicio, goPagos1, shipping_view, confirmacion_pago

urlpatterns = [
    path('home/', inicio, name='inicio'),
    path('index/', goIndex, name="index"),
    path('pagos/', goPagos1, name='pagos1'),
    path('envio/', shipping_view, name='shipping_view'),
    path('confirmacion/<int:payment_id>/', confirmacion_pago, name='confirmacion_pago'),
]