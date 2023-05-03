from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .form import EmprendedorForms, ConsumidorForms, ProductoForms, ContactoForms
from .models import Emprendedor, Consumidor, Categorias, Propietarios, Producto
from django.contrib.auth.decorators import login_required
# import vonage
from twilio.rest import Client


def home(request):
    listaCategorias = Categorias.objects.all()
    context = {'listaCategorias': listaCategorias}
    return render(request, "home.html", context)


def contactanos(request):

    if request.method == 'POST':
        form = ContactoForms(request.POST, request.FILES)
        if form.is_valid():
            # account_sid = 'AC6b6ffc0469b49c70652ce4bb9014adb3'
            account_sid = 'AC6b6ffc0469b49c70652ce4bb9014adb3'
            # print(settings.ACCOUNT_SID_TWILIO)
            # auth_token = '4fc8e454be511d81e386d4fbe5031757'
            auth_token = 'f33ade014c543cc32b2a5351d07488c3'
            # print(settings.TOKEN_TWILIO)
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=form.cleaned_data['mensaje'],
                to='whatsapp:+59164888167'
            )
            # return render(request, 'contactanos.html')
            return redirect('contactanos')
    else:
        form = ContactoForms()
    context = {'form': form}
    return render(request, 'contactanos.html', context)


def acerca_nosotros(request):
    propietarios = Propietarios.objects.all()
    context = {'propietarios': propietarios}
    return render(request, 'acerca_nosotros.html', context)


def registrar(request):
    if request.method == 'POST':
        form = EmprendedorForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = EmprendedorForms()
    context = {'form': form}
    return render(request, 'registrar.html', context)


def registrar_consumidor(request):
    if request.method == 'POST':
        form = ConsumidorForms(request.POST, request.FILES)
        # if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    else:
        form = ConsumidorForms()
    context = {'form': form}
    return render(request, 'registrar_consumidor.html', context)


def pagina_registro(request):
    return render(request, 'pagina_registro.html')


def inicar_sesion(request):
    return render(request, 'iniciar_sesion.html', {'form': AuthenticationForm})


def cerrar_sesion(request):
    logout(request)
    return redirect('home')


@login_required
def perfil(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'perfil.html', context)


@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProductoForms()
    context = {'form': form}
    return render(request, 'crear_producto.html', context)


def lista_usuarios(request):
    listaEmp = Emprendedor.objects.all()
    listaCons = Consumidor.objects.all()
    context = {'listaEmp': listaEmp,
               'listaCons': listaCons, }
    return render(request, 'lista_usuarios.html', context)


def condiciones(request):
    return render(request, 'condiciones.html')


def privacidad(request):
    return render(request, 'privacidad.html')


def buscar_por_categoria(request, categoria_id):
    # query = request.GET.get('q')
    # resultados = Producto.objects.filter(Q(nombre_producto__icontains=query))
    resultados = Producto.objects.filter(categoria=categoria_id)
    return render(request, 'buscar_por_categoria.html', {'resultados': resultados})
