from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

def inicio(request):
    return render(request, "FECODER_APP/inicio.html")

def usuarios(request):
    return render(request, "FECODER_APP/usuarios.html")

def posts(request):
    return render(request, "FECODER_APP/posts.html")

def categorias(request):
    return render(request, "FECODER_APP/categorias.html")

def formularioUsuarios(request):
    if request.method == 'POST':

        miFormulario = formularioUsuario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre_usuario = informacion['nombre_usuario'], clave_usuario = informacion['clave_usuario'], correo_usuario = informacion['correo_usuario'])
            usuario.save()
            return render(request, 'FECODER_APP/inicio.html')
    else:
        miFormulario = formularioUsuario()

    return render(request, 'FECODER_APP/usuarios.html',{"miFormulario":miFormulario})
