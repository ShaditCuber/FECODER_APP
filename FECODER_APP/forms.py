from django import forms

class formularioUsuario(forms.Form):
    nombre_usuario = forms.CharField()
    clave_usuario = forms.CharField(widget=forms.PasswordInput())
    clave_verificar_usuario = forms.CharField(widget=forms.PasswordInput())
    correo_usuario = forms.EmailField()

class formularioComentario(forms.Form):
    comentario_post = forms.CharField()