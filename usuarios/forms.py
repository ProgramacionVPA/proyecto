from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Ruta

class FormularioRegistro(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

class FormularioRuta(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['origen', 'destino', 'hora_salida', 'dias', 'cupos_disponibles']