from django.urls import path
from .views import *

urlpatterns = [
    path('', perfil, name='perfil'),
]
