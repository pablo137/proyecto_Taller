from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .form import EmprendedorForms, ConsumidorForms, ProductoForms
from .models import Emprendedor, Consumidor, Categorias, Propietarios, Producto
from django.contrib.auth.decorators import login_required
# import vonage
from twilio.rest import Client


def home(request):
    listaCategorias = Categorias.objects.all()
    context = {'listaCategorias': listaCategorias}
    return render(request, "home.html", context)


def contactanos(request):
    ##################################################################
    # client = vonage.Client(key="3a6b1505", secret="clLJALboB46d51Nt")
    # sms = vonage.Sms(client)
    # responseData = sms.send_message({"from": "Vonage APIs", "to": "59164888167", "text": "A text message sent using the Nexmo SMS API",})
    # if responseData["messages"][0]["status"] == "0":
    #     print("Message sent successfully.")
    # else:
    #     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    ###################################################################

    account_sid = 'AC6b6ffc0469b49c70652ce4bb9014adb3'
    auth_token = '291ba083612ef3021a0fc683ed0c6d5a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Esto de los mensajes es interesante. Lo malo es que no tiene la marca de Oneclick. Mañana avancemos el proyecto que dices. Atte. PABLO',
        to='whatsapp:+59177606087'
    )

    print(message.sid)

    return render(request, 'contactanos.html')


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
