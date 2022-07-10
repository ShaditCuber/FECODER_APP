from django import forms

class formularioUsuario(forms.Form):
    nombre_usuario = forms.CharField()
    clave_usuario = forms.CharField()
    correo_usuario = forms.EmailField()