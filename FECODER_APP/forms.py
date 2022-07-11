from django import forms

class formularioUsuario(forms.Form):
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    clave_usuario = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    clave_verificar_usuario = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    correo_usuario = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}))

class formularioComentario(forms.Form):
    comentario_post = forms.CharField()