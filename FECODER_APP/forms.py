from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget




class formularioPost(forms.Form):
    titulo_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Felipe'}))
    subtitulo_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Tecnologia'}))
    contenido_post = forms.CharField(widget = CKEditorWidget())
    imagen_post = forms.ImageField(required=False)

class edicionPost(forms.Form):
    titulo_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Felipe'}))
    subtitulo_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Tecnologia'}))
    contenido_post = forms.CharField(widget = CKEditorWidget())
    imagen_post = forms.ImageField(required=False)
    


class formularioContacto(forms.Form):
    nombre_contacto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Felipe'}))
    celular_contacto = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 12345678', 'type': 'number'}))
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

class editarUsuario(forms.Form):

    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electrónico',
            }
    )
    )
    

    first_name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    last_name = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "avatar"]
        help_texts ={k:"" for k in fields}

class editarContraseña(PasswordChangeForm):
    old_password = forms.CharField(
        label="Contraseña Antigua",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
        help_text=("Por favor, escribe la contraseña antigua."),
    )
    new_password1 = forms.CharField(
        label="Contraseña Nueva",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        help_text=("Contraseña de al menos 8 caracteres."),
    )
    new_password2 = forms.CharField(
        label="Confirmacion Contraseña",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=("Por favor, escribe la misma contraseña anterior."),
    )
    error_messages = {
        "password_mismatch": "Las contraseñas no coinciden.",
        "password_incorrect": "La contraseña antigua es incorrecta.",
    }
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
        help_texts ={k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen=forms.ImageField()
