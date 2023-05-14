from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('productos/', productos, name='productos'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('register/', registrar, name='register'),
]
