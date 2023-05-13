from django.db import models
from django.utils.timezone import now

opciones_contacto = [
    [0, 'Pedir informacion'],
    [1, 'Mandar una queja'],
    [3, 'Sugerir, recomendar'],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre y Apellido:')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Mensaje')
    contacto_tipo = models.IntegerField(choices=opciones_contacto, default=opciones_contacto[0], verbose_name='Tipo de Contacto')
    subscripcion = models.BooleanField(default=False, verbose_name='Recibir correos de productos e informacion')
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envio')