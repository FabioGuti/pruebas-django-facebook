from django.forms import ModelForm
from django import forms

class MensajeForm(forms.Form):
    mensaje = forms.CharField(label = "Escribe un mensaje", widget = forms.Textarea)
