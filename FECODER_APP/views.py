from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

def inicio(request):
    return render(request, "FECODER_APP/inicio.html")

""" def usuarios(request):
    return render(request, "FECODER_APP/usuarios.html") """

def posts(request):
    return render(request, "FECODER_APP/posts.html")

def categorias(request):
    return render(request, "FECODER_APP/categorias.html")

def formularioUsuarios(request):
    print("Entro a formularioUsuarios")
    if request.method == 'POST':

        miFormulario = formularioUsuario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario = informacion['nombre_usuario']
            clave = informacion['clave_usuario']
            clave_verificar = informacion['clave_verificar_usuario']
            correo = informacion['correo_usuario']
            if clave.__eq__(clave_verificar):
                usuario = Usuario(nombre_usuario=usuario, clave_usuario=clave, 
                                    clave_verificar_usuario=clave_verificar, correo_usuario=correo)
                usuario.save()
                return render(request, 'FECODER_APP/inicio.html')
            return render(request, 'FECODER_APP/formularioUsuarios.html',{"error":"Contraseña no coincide","miFormulario":miFormulario})
    else:
        miFormulario = formularioUsuario()

        return render(request, 'FECODER_APP/formularioUsuarios.html',{"miFormulario":miFormulario})


def formularioComentarios(request):
    if request.method == 'POST':

        miFormulario = formularioComentario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            comentario=Comentario(comentario=informacion['comentario'])    
            return render(request, 'FECODER_APP/inicio.html')
    else:
        miFormulario = formularioUsuario()

        return render(request, 'FECODER_APP/formularioComentarios.html',{"miFormulario":miFormulario})

#buscar comentario
def buscarUsuariox(request):
    
    usuario=request.GET['nombre']
    if usuario!="":
        obj = Usuario.objects.filter(nombre_usuario=usuario)
        return render(request, 'FECODER_APP/inicio.html',{'usuario':obj,'nombre':usuario})
    else:
         return render(request, 'FECODER_APP/inicio.html',{"error":"No se ingreso un nombre de usuario"})


def buscarUsuario(request):
         return render(request, 'FECODER_APP/inicio.html')