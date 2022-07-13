from django import forms

class formularioUsuario(forms.Form):
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Pepe'}))
    clave_usuario = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Máximo 8 caracteres'}))
    clave_verificar_usuario = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Las contraseñas deben coincidir'}))
    correo_usuario = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}))


class formularioComentario(forms.Form):
    comentario_post = forms.CharField()


class formularioPost(forms.Form):
    titulo_post = forms.CharField()
    fecha_post = forms.DateField()
    contenido_post = forms.CharField()
    estatus_post = forms.BooleanField()


class formularioCategoria(forms.Form):
    nombre_categoria = forms.CharField()
