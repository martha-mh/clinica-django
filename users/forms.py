from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        }),
        error_messages={'required': 'Por favor ingresa tu nombre de usuario.'}
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }),
        error_messages={'required': 'Por favor ingresa tu contraseña.'}
    )

    def non_field_errors(self):
        errors = super().non_field_errors()
        if errors:
            return self.error_class(['Usuario y/o contraseña incorrectos.'])
        return errors