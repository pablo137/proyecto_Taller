from django import forms
from .models import Contacto

class ContactoForms(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = '__all__' #-> muestra todos los campos 
        fields = ['nombre',
                  'email',
                  'message',
                  'contacto_tipo',
                  'subscripcion',
                  ]
