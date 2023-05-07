from django.urls import path
from login.views import crear_usuario

urlpatterns = [
    path('crear_usuario', crear_usuario, name='crear_usuario'),
]
