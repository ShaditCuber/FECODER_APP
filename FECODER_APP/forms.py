from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget




class formularioPost(forms.Form):
    titulo_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Felipe'}))
    subtitulo_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Tecnologia'}))
    contenido_post = forms.CharField(widget = CKEditorWidget())
    imagen_post = forms.ImageField()
    


class formularioContacto(forms.Form):
    nombre_contacto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Pepe'}))
    celular_contacto = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 12345678'}))
    correo_contacto = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com' }))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Lorem Impsum '}))


#Clases para login, registro y logout
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(
        label='Nombre de Usuario',
        widget=forms.TextInput(attrs={"class":"form-control"}))

    password = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"form-control"}),
        
    )
    error_messages = {
        "invalid_login": 
            "Por favor, introduzca un nombre de usuario y contraseña correctos. Considere que ambos campos son sensibles al uso de mayúsculas."
        ,
        "inactive": "Esta cuenta esta inactiva.",
    }
    
    class Meta:
        model = User
        fields = ["username", "password","error_messages"]
        help_texts ={k:"" for k in fields}

class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electrónico',
            }
    )
    )
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        help_text=("Contraseña de al menos 8 caracteres."),
    )
    password2 = forms.CharField(
        label=("Confirmacion Contraseña"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=("Por favor, escribe la misma contraseña anterior."),
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2" ]
        help_texts ={k:"" for k in fields}