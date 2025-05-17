from django.urls import path
from .views import home, homeHTML, index, detalle_categoria

urlpatterns = [
    path('home/', home, name='home'),
    path('homeDOS/', homeHTML, name='homeDOS'),
    path('index/', index, name='index'),
    path('index/<int:id>/', detalle_categoria, name='detalle_categoria'),
]