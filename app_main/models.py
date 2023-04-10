from django.db import models

class Emprendedor(models.Model):
    nombre_completo = models.CharField(help_text="Introduce tu nombre completo",max_length=200)
    nit = models.IntegerField()
    correo = models.EmailField()
    numero_telefono: models.CharField(max_length=20)
    numero_cuenta_bancaria: models.IntegerField()
    banco = models.CharField(max_length=20)
    img_perfil = models.ImageField(upload_to="emprendedores/", null=True)
    direccion = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f"Emprendedor: {self.nombre_completo}"

class Consumidor(models.Model):
    nombre_completo = models.CharField(help_text="Introduce tu nombre completo",max_length=200)
    nit = models.IntegerField()
    correo = models.EmailField()
    numero_telefono: models.CharField(max_length=20)
    banco = models.CharField(max_length=20)
    numero_cuenta_bancaria: models.IntegerField()
    img_perfil = models.ImageField(upload_to="consumidores/", null=True)
    print(img_perfil)
    # fecha_nacimiento = models.DateTimeField(blank=True)
    def __str__(self) -> str:
        return f"Consumidor: {self.nombre_completo}"
    
class Categorias(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    img_categoria = models.ImageField(upload_to="categoria/", null=True)