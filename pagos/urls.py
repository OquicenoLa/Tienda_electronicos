from django.urls import path
from .views import goIndex, inicio, goPagos1

urlpatterns = [
    path('home/', inicio, name='inicio'),
    path('index/', goIndex, name="index"),
    path('pagos/', goPagos1, name='pagos1')
]