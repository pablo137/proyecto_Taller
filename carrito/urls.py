from django.urls import path
from .views import carrito, agregar_carrito, eliminar_carrito, reducir_cantidad, limpiar_carrito

urlpatterns = [
    path('', carrito, name='carrito'),
    path('agregar/<int:producto_id>/', agregar_carrito, name='addCarrito'),
    path('eliminar/<int:producto_id>/', eliminar_carrito, name='removeCarrito'),
    path('reducir/<int:producto_id>/', reducir_cantidad, name='reducirCarrito'),
    path('limpiar/', limpiar_carrito, name='limpiarCarrito'),
]
