from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Productos, Categorias
from .forms import ProductoForms
# Create your views here.

@login_required
def producto(request):
    context = {'titulo': 'Productos',
               'datos': Productos.objects.all(),}
    return render(request, 'productos.html',context)

@login_required
def registrar_producto(request, id):
    pass

@login_required
def eliminar_producto(request,id):
    products = Productos.objects.get(id=id)
    products.delete()

@login_required
def editar_producto(request,id):
    # products = get_object_or_404(Productos, id=id)
    productos = Productos.objects.get(id=id)
    context = {'titulo':'Edicion de producto',
               'productos': productos,
               }
    return render(request,'editar_producto.html', context)