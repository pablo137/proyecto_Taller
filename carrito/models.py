from django.db import models
from producto.models import Productos
from django.contrib.auth.models import User

# Create your models here.
class Carrito(models.Model):
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='carrito')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    nombre = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nombre de producto')
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(default='productos/img_defecto_cpzv2f.jpg', upload_to='productos/', verbose_name='Imagen de producto')

    def __str__(self):
        return "Producto: {0}, Cantidad: {1}, Precio:{2}".format(self.nombre, self.cantidad, self.precio)