from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm

def home(request):
    context = {'titulo': 'Home',
               'saludo': 'Hola desde Home'}
    return render(request, 'home.html', context)

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