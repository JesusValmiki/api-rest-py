# from django.forms import ModelForm
# from .models import Contacto
# # from django import forms

# class ContactForm(ModelForm):
#     class Meta:
#         model = Contacto
#         fields = ['nombre', 'email', 'mensaje']
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contacto

class ContactForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Escribe tu nombre aquí'}),
            'email': EmailInput(attrs={'placeholder': 'Escribe tu correo electrónico'}),
            'mensaje': Textarea(attrs={'placeholder': 'Escribe tu mensaje'}),
        }