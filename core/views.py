from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm
from producto.models import Categorias, Productos

def home(request):
    # context = {'titulo': 'Home',
    #            'saludo': 'Hola desde Home'}
    listaCategorias = Categorias.objects.all()
    context = {'listaCategorias': listaCategorias}
    return render(request, 'home.html', context)

def buscar_por_categoria(request, categoria_id):
    # query = request.GET.get('q')
    # resultados = Producto.objects.filter(Q(nombre_producto__icontains=query))
    resultados = Productos.objects.filter(categoria=categoria_id)
    return render(request, 'buscar_por_categoria.html', {'resultados': resultados})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def registrar(request):
    context =  { 'form' : CustomUserCreationForm()}
    if request.method == 'POST':
        user_creado_form = CustomUserCreationForm(data=request.POST)
        if user_creado_form.is_valid():
            user_creado_form.save()

            user = authenticate(username=user_creado_form.cleaned_data['username'], password=user_creado_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html', context)