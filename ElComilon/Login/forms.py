from django import forms
from models import Cliente

class formlog(forms.ModelForm):
    class Meta:
        models = Cliente
        field = ["nombreusuario", "contrasena"]