from django import forms
from django.http import request
from .models import Artwork, Order


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'image', 'price']


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        # Obtiene de la sesión el total
        total_float = self.request.session.get('total_float')
        super().__init__(*args, **kwargs)
        self.fields["total"].initial = total_float

    class Meta:
        model = Order
        fields = ['email', 'name', 'address', 'suburb', 'total']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion, calle y numero'}),
            'suburb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia o fraccionamiento'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
