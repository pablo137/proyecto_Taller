from django.urls import path
from .views import *

urlpatterns = [
    path('', producto, name='productos'),
    path('registrarProducto/', registrar_producto, name='registrar_producto'),
    path('eliminarProducto/<int:id>', eliminar_producto, name='eliminar_producto'),
    path('editarProducto/<int:id>', editar_producto, name='editar_producto'),
]