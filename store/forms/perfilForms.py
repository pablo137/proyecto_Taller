from django import forms
from store.models.perfil import UserProfile
from store.models.customer import Customer

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['img', 'bio']


class MyUserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email']