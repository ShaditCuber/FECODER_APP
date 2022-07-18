from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from datetime import datetime

#Inicio
def inicio(request):
    #ordenado por contenido post
    return render(request, "FECODER_APP/inicio.html",{'todos_post':Post.objects.order_by('contenido_post'),'first_post':Post.objects.first(),'miFormulario':formularioContacto()})

#Formularios
def formularioUsuarios(request):
    
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
                miFormulario = formularioUsuario()
                return render(request, 'FECODER_APP/formularioUsuarios.html',{"usuarioCreado":usuario,"miFormulario":miFormulario})
            return render(request, 'FECODER_APP/formularioUsuarios.html',{"error":"Contraseña no coincide","miFormulario":miFormulario})
    else:
        miFormulario = formularioUsuario()

        return render(request, 'FECODER_APP/formularioUsuarios.html',{"miFormulario":miFormulario})

def formularioPosts(request):
    if request.method == 'POST':

        miFormulario = formularioPost(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            try:

                    post = Post(titulo_post = informacion['titulo_post'], fecha_post =informacion['fecha_post'] , contenido_post = informacion['contenido_post'] , estatus_post = informacion['estatus_post'])

                    post.save()

                    miFormulario = formularioPost()

                    return render(request, 'FECODER_APP/formularioPosts.html', {"postCreado":post,"miFormulario":miFormulario})    
            except ValueError:
                    
                    return render(request, 'FECODER_APP/formularioPosts.html', {"error":"Formato de fecha incorrecto","miFormulario":miFormulario})
            
    else:
        miFormulario = formularioPost()

        return render(request, 'FECODER_APP/formularioPosts.html', {"miFormulario":miFormulario})

def formularioContactos(request):
    if request.method == 'POST':

        miFormulario = formularioContacto(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            contacto = Contacto(nombre_contacto = informacion['nombre_contacto'], celular_contacto =informacion['celular_contacto'] ,correo_contacto=informacion['correo_contacto'], mensaje=informacion['mensaje'])
            contacto.save()

            miFormulario = formularioContacto()

            return render(request, 'FECODER_APP/inicio.html', {"contactoCreado":contacto,"miFormulario":miFormulario})    
            
                    
                   
            
    else:
        miFormulario = formularioContacto()

        return render(request, 'FECODER_APP/inicio.html', {"miFormulario":miFormulario})

#Buscar


def buscandoPost(request):
    post=request.GET['titulo']
    if post!="":
        obj = Post.objects.filter(titulo_post__icontains=post).first()
        
        if obj: 
            
            return render(request, 'FECODER_APP/inicio.html',{'post':obj,'titulo':post,'todos_post':Post.objects.all(),'miFormulario':formularioContacto()})

        return render(request, 'FECODER_APP/inicio.html',{'x':"No existe post con el nombre "+post,'todos_post':Post.objects.all(),'first_post':Post.objects.first(),'miFormulario':formularioContacto()})
    else:
         return render(request, 'FECODER_APP/inicio.html',{"error":"No se ingreso un nombre de post",'todos_post':Post.objects.all(),'first_post':Post.objects.first(),'miFormulario':formularioContacto()})

def buscarPost(request):
         return render(request, 'FECODER_APP/inicio.html')


def buscandoUsuario(request):
    todos_post=Post.objects.all()
    usuario=request.GET['nombre']
    if usuario!="":
        obj = Usuario.objects.filter(nombre_usuario__icontains=usuario)
        if obj: 
            return render(request, 'FECODER_APP/inicio.html',{'usuario':obj,'nombre':usuario,'todos_post':todos_post,'first_post':Post.objects.first(),'miFormulario':formularioContacto()})
   
        return render(request, 'FECODER_APP/inicio.html',{'x':"No existe usuario con el nombre "+usuario,'todos_post':todos_post,'first_post':Post.objects.first(),'miFormulario':formularioContacto()})
    else:
         return render(request, 'FECODER_APP/inicio.html',{"error":"No se ingreso un nombre de usuario",'todos_post':todos_post,'first_post':Post.objects.first(),'miFormulario':formularioContacto()})


def buscarUsuario(request):
         return render(request, 'FECODER_APP/inicio.html')


def buscandoContacto(request):
    nombre=request.GET['nombre']
    if nombre!="":
        obj = Contacto.objects.filter(nombre_contacto__icontains=nombre)
        if obj: 
            return render(request, 'FECODER_APP/buscarContacto.html',{'contacto':obj,'nombre':nombre})
   
        return render(request, 'FECODER_APP/buscarContacto.html',{'x':"No existe contacto con el nombre "+nombre})
    else:
         return render(request, 'FECODER_APP/buscarContacto.html',{"errorContacto":"No se ingreso un nombre de contacto"})
         
def buscarContacto(request):
         return render(request, 'FECODER_APP/buscarContacto.html')



def login(request):
    return render(request, 'FECODER_APP/login.html')


def registro(request):
    return render(request, 'FECODER_APP/registro.html')