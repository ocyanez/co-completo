from django import forms
from .models import Contacto, Producto


class ContactoFrom(forms.ModelForm):
    class Meta:
        model: Contacto
        #model = ["nombre", "correo", "motivo", "mensaje"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'