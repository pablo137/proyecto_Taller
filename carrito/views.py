from django.shortcuts import render, redirect
from .cart import Carrito
from producto.models import Productos

# Create your views here.
def carrito(request):
    context = { 'titulo': 'Carrito',}
    return render(request, 'carrito.html', context)


def agregar_carrito(request, product_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=product_id)
    carrito.add(producto)
    return redirect('productos')

def eliminar_carrito(request, product_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=product_id)
    carrito.remove(producto)
    return redirect('productos')

def reducir_cantidad(request, product_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=product_id)
    carrito.decrementar(producto)
    return redirect('productos')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect('productos')