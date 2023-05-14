from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactoForms

def contacto(request):
    context = { 'titulo': 'Contacto',
               'form':ContactoForms()}
    if request.method == 'POST':
        contacto_form = ContactoForms(data=request.POST)
        if contacto_form.is_valid():
            contacto_form.save()

            return redirect(reverse('contacto')+'?ok')
        else:
            return redirect(reverse('contacto')+'?error')

    return render(request, 'contacto.html',context)
