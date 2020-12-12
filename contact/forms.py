from django import forms
from .models import Form

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", min_length=3, max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tu nombre'}))
    email = forms.EmailField(label="Email", min_length=5, max_length=100, required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingresa tu correo electrónico'}))
    message = forms.CharField(label="Mensaje", min_length=5, max_length=300, required=True, widget=forms.Textarea(attrs={'placeholder':'Dejanos tu mensaje','rows':5}))

    class Meta:
        model = Form
        exclude = ('created')
