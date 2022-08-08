from django import forms


class MensajeForm(forms.Form):
    texto = forms.CharField( widget=forms.TextInput
                            (attrs={'class': 'flex-1 mr-3', 'placeholder': 'Escribe un mensaje','type':'text'}))
    
    