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
    def __str__(self) -> str:
        return self.nombre_categoria

class Propietarios(models.Model):
    nombre = models.CharField(max_length=100)
    numTelefono = models.CharField(max_length=50, null=True)
    correo = models.EmailField(blank=True)    
    cargo = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Propietarios/", null=True)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}"

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, default=None)
    descripcion = models.TextField(max_length=200)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    descuento = models.CharField(max_length=5)
    img_producto = models.ImageField(upload_to="Productos/", null=True)
    def __str__(self) -> str:
        return f"{self.nombre_producto}, Categoria: {self.categoria}"