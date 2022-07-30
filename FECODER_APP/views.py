from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from datetime import datetime
from django.contrib.auth  import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

#Inicio
def inicio(request):
    #ordenado por contenido post
    try:
        if not Avatar.objects.filter(user=request.user)[0].imagen.name=='default.jpg':
            avatar=Avatar.objects.filter(user=request.user)
            img=avatar[0].imagen.url
    except:
            img=''



    if Post.objects.all()!=None:
        todos_post=todosPost()
        first_post=primerPost('')
    else :
        todos_post=''
        first_post=''        
    
    return render(request, 'FECODER_APP/inicio.html',{'todos_post':todos_post,'first_post':first_post,'miFormulario':formularioContacto(),'avatar':img})
    

#Formularios
""" def formularioUsuarios(request):
    
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

        return render(request, 'FECODER_APP/formularioUsuarios.html',{"miFormulario":miFormulario}) """

@login_required
def formularioPosts(request):
    if request.method == 'POST':

        miFormulario = formularioPost(request.POST,request.FILES)
        
        if miFormulario.is_valid():
            print("valido")
            informacion = miFormulario.cleaned_data
            

            post = Post(
                        usuario_post=request.user,
                        titulo_post = informacion['titulo_post'],
                        subtitulo_post = informacion['subtitulo_post'],
                        fecha_post =datetime.now() ,
                        contenido_post = informacion['contenido_post'] ,
                        estatus_post = True,
                        imagen_post = informacion['imagen_post']
                        )

            post.save()

            miFormulario = formularioPost()

            return render(request, 'FECODER_APP/formularioPosts.html', {"postCreado":post,"form_post":miFormulario})    
            
            
    else:
        miFormulario = formularioPost()

        return render(request, 'FECODER_APP/formularioPosts.html', {"form_post":miFormulario})

def formularioContactos(request):
    if request.method == 'POST':

        miFormulario = formularioContacto(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            contacto = Contacto(nombre_contacto = informacion['nombre_contacto'], celular_contacto =informacion['celular_contacto'] ,correo_contacto=informacion['correo_contacto'], mensaje=informacion['mensaje'])
            contacto.save()

            miFormulario = formularioContacto()

            return render(request, 'FECODER_APP/inicio.html', {"contactoCreado":contacto,"miFormulario":miFormulario,'todos_post':Post.objects.order_by('contenido_post'),'first_post':Post.objects.first()})    
            
                    
                   
            
    else:
        miFormulario = formularioContacto()

        return render(request, 'FECODER_APP/inicio.html', {"miFormulario":miFormulario,'todos_post':Post.objects.order_by('contenido_post'),'first_post':Post.objects.first()})

#Buscar


def buscandoPost(request):
    post=request.GET['titulo']
    todos_post=todosPost()
    primer_post=primerPost(post)
    if post!="":
        obj = Post.objects.filter(estatus_post=True).filter(titulo_post__icontains=post).first()
        
        if obj: 
            return render(request, 'FECODER_APP/inicio.html',{'post':obj,'titulo':post,'todos_post':todos_post,'first_post':obj,'miFormulario':formularioContacto()})

        return render(request, 'FECODER_APP/inicio.html',{'x':"No existe post con el nombre "+post,'todos_post':todos_post,'first_post':primer_post,'miFormulario':formularioContacto()})
    else:
         return render(request, 'FECODER_APP/inicio.html',{"error":"No se ingreso un nombre de post",'todos_post':todos_post,'first_post':primer_post,'miFormulario':formularioContacto()})

def buscarPost(request):
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



def loginUser(request):
    redirect_to = request.POST.get('next', '')
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                todos_post=todosPost()
                primer_post=primerPost('')
                return render(request, 'FECODER_APP/inicio.html',{'todos_post':todos_post,'first_post':primer_post,'miFormulario':formularioContacto()})
                             
        else:
            return render(request, 'FECODER_APP/login.html',{'form_login':form,'mensaje':f"Usuario o contraseña incorrectos"})
        
    else:
        form = LoginForm()
        return render(request, 'FECODER_APP/login.html', {'form_login': form})


def registroUser(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            avatar=Avatar(user=User.objects.get(username=username))
            #USAR PARA CAMBIAR NOMBRE DE FOTO A ID DE USUARIO
            # avatar.imagen.name=username+".png"
            avatar.save()
            return render(request, 'FECODER_APP/login.html',{'mensaje_login':f"Usuario registrado correctamente {username}"})
        
        return render(request, 'FECODER_APP/registro.html',{'form_register':form,'error':form.errors})

    else:
        form = RegisterForm()
        return render(request, 'FECODER_APP/registro.html', {'form_register': form})



def logoutUser(request):
    todos_post=todosPost()
    primer_post=primerPost('')
    logout(request)
    return render(request, 'FECODER_APP/inicio.html',{'todos_post':todos_post,'first_post': primer_post, 'miFormulario':formularioContacto()})

def editarUsuario(request,id):
    if request.method == 'POST':
        form = EditarForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request, 'FECODER_APP/login.html',{'mensaje_login':f"Usuario editado correctamente {username}"})
        
        return render(request, 'FECODER_APP/editar.html',{'form_editar':form,'error':form.errors})

    else:
        form = EditarForm()
        return render(request, 'FECODER_APP/editar.html', {'form_editar': form})

def verPost(request,id):
    post=Post.objects.get(id=id)
    avatar = Avatar.objects.filter(user = post.usuario_post)
    return render(request, 'FECODER_APP/mostrarPost.html',{'post':post,'img':avatar[0].imagen})

def borrarPost(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return render(request, 'FECODER_APP/inicio.html',{'todos_post':todosPost(),'first_post':primerPost(''),'miFormulario':formularioContacto()})

def editarPost(request,id):
    post=Post.objects.get(id=id)
    if request.method == 'POST':
        form = formularioPost(request.POST,request.FILES)
        if form.is_valid():
            post.titulo_post=form.cleaned_data['titulo_post']
            post.contenido_post=form.cleaned_data['contenido_post']
            post.subtitulo_post=form.cleaned_data['subtitulo_post']
            post.imagen_post=form.cleaned_data['imagen_post']
            post.estatus_post=form.cleaned_data['estatus_post']
            post.save()
            return render(request, 'FECODER_APP/inicio.html',{'todos_post':todosPost(),'first_post':primerPost(''),'miFormulario':formularioContacto()})
        
    else:
        form = formularioPost(initial={'titulo_post':post.titulo_post,'contenido_post':post.contenido_post,'subtitulo_post':post.subtitulo_post,'imagen_post':post.imagen_post,'estatus_post':post.estatus_post})
        return render(request, 'FECODER_APP/editarPost.html',{'form_post':form,'post':post})

def desactivarPost(request,id):
    post=Post.objects.get(id=id)
    if post.estatus_post:
        post.estatus_post=False
        post.save()
    else :
        post.estatus_post=True
        post.save()

    
    posts= Post.objects.filter(usuario_post=request.user).order_by('fecha_post')
    avatar = Avatar.objects.filter(user = request.user)
    return render(request, 'FECODER_APP/todosPostsUser.html',{'posts':posts,'img':avatar[0].imagen})



def todosPostsUser(request):
    posts= Post.objects.filter(usuario_post=request.user).order_by('fecha_post')
    avatar = Avatar.objects.filter(user = request.user)
    return render(request, 'FECODER_APP/todosPostsUser.html',{'posts':posts,'img':avatar[0].imagen})

def todosPost():
    return Post.objects.filter(estatus_post=True).order_by('contenido_post')

def primerPost(tema):
   
    if Post.objects.all()!=None:
        if tema!='':
            if Post.objects.filter(estatus_post=True).filter(titulo_post__icontains=tema).first() :
                return Post.objects.filter(estatus_post=True).filter(titulo_post__icontains=tema).first()
            else:
                return Post.objects.filter(estatus_post=True).first()
        else:
        
            return Post.objects.filter(estatus_post=True).first()
    
