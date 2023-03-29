from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import  AuthenticationForm
from .form import EmprendedorForms, ConsumidorForms
from .models import Emprendedor, Consumidor


def home(request):
    return render(request, "home.html")


def contactanos(request):
    return render(request, 'contactanos.html')


def acerca_nosotros(request):
    return render(request, 'acerca_nosotros.html')


def registrar(request):
    if request.method == 'POST':
        form = EmprendedorForms(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['nombre_completo']
            return redirect('perfil')
    else:
        form = EmprendedorForms()
    context = {'form': form}
    return render(request, 'registrar.html', context)

def registrar_consumidor(request):
    if request.method == 'POST':
        form = ConsumidorForms(request.POST)
        # if form.is_valid():
        form.save()
        nombre = form.cleaned_data['nombre_completo']
        return redirect('perfil')
    else:
        form = ConsumidorForms()
    context = {'form': form}
    return render(request, 'registrar_consumidor.html', context)


def pagina_registro(request):
    return render(request,'pagina_registro.html')

def inicar_sesion(request):
    return render(request, 'iniciar_sesion.html',{ 'form' : AuthenticationForm})


def perfil(request):
    listaEmp = Emprendedor.objects.all()
    listaCons = Consumidor.objects.all()
    context = {'listaEmp': listaEmp,
               'listaCons': listaCons,}
    return render(request, 'perfil.html', context)
