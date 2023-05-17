from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('productos/', productos, name='productos'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('register/', registrar, name='register'),
    path('buscar_por_categoria/<int:categoria_id>/', buscar_por_categoria, name='buscar_por_categoria'),
]
