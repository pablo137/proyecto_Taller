from django import forms
from store.models.perfil import UserProfile
from store.models.customer import Customer
from store.models.product import Product


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["img", "bio"]


class MyUserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "phone", "email"]


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "image",
            "price",
            "stock",
        ]
