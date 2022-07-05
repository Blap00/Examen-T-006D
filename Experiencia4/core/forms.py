
from django import forms
from django.forms import ModelForm
from .models import Usuarios, FormSolicitud


class RegisterForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['username', 'mail', 'password']
        widgets = {
            'mail':forms.EmailInput(attrs={'required':'required'}),
            'password':forms.TextInput(attrs={'required':'required'}),
        }

class SolicitudesForm(ModelForm):
    class Meta:
        model = FormSolicitud
        fields = ['nombreCompleto', 'mailSolicitante', 'descripcion']

        