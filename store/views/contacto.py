from django.shortcuts import render, redirect
from django.urls import reverse
from store.forms.perfilForms import ContactoForms
from django.core.mail import EmailMessage

def contacto(request):
    # print('Tipo de petición: {}'.format(request.method))
    contact_form = ContactoForms()
    
    if request.method == 'POST':
        # Estoy enviando el formulario
        contact_form = ContactoForms(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('nombre', '')
            email = request.POST.get('correo', '')
            message = request.POST.get('mensaje', '')

            # Enviar el correo electrónico
            email = EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                email,
                ['523a1a06ac16bd@inbox.mailtrap.io'],
                reply_to=[email],
            )
            
            try:
                email.send()
                # Está todo OK
                return redirect(reverse('contacto')+'?ok')
            except:
                # Ha habido un error y retorno a ERROR
                return redirect(reverse('contacto')+'?error')

    return render(request, 'contacto.html', {'form':contact_form}) 