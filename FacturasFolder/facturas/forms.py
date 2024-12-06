from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'nombre',
            'monto',
            'metodo',
            'documento_identidad',
        ]

        labels = {
            'nombre':"Nombre",
            'monto':"Monto",
            'metodo':"Metodo",
            'documento_identidad':"Documento_identidad",
        }