from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistroForm(UserCreationForm):
    #sobreescribir el campo email para hacerlo obligatorio y usar nuestro CustomUser
    email = forms.EmailField(
        required=True,
        label='Correo Electronico',
        max_length=254, 
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese correo electronico")
        return email

class LoginForm(AuthenticationForm):
    #se esta usando el formulario de autenticacion de django
    pass