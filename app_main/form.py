from django import forms
from .models import Emprendedor,Consumidor

class EmprendedorForms(forms.ModelForm):
    nit = forms.IntegerField(label="NIT")
    correo = forms.EmailField(label="Correo electronico")
    banco = forms.CharField(label='Nombre Banco', max_length=20)
    numero_telefono = forms.CharField(label='Numero de telefono', max_length=10)
    numero_cuenta_bancaria = forms.IntegerField(label="Numero de cuenta bancaria")
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contrasenia", widget=forms.PasswordInput)
    class Meta:
        model = Emprendedor
        fields = [
            'nombre_completo',
            'nit',
            'correo',
            'numero_telefono',
            'banco',
            'numero_cuenta_bancaria',
            'img_perfil',
            'direccion',
            'rubro',
            'descripcion',
            'password1',
            'password2',
        ]

class ConsumidorForms(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = '__all__'