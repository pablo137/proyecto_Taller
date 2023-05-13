from django import forms
from .models import Categorias, Productos

class ProductoForms(forms.ModelForm):
    class Meta:
        model : Productos
        fields = '__all__'
