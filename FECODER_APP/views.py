from tkinter import N
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



    if Post.objects.all()!=None:
        todos_post=todosPost()
        first_post=primerPost('')
    else :
        todos_post=''
        first_post=''        
    
    return render(request, 'FECODER_APP/inicio.html',{'todos_post':todos_post,'first_post':first_post,'formularioContacto':formularioContacto(),'avatar':img(request)})
    

#Formularios


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
                        )

            if informacion['imagen_post']!=None:
                 post.imagen_post=informacion['imagen_post']
            

            post.save()

            miFormulario = formularioPost()

            return render(request, 'FECODER_APP/post/formularioPosts.html', {"postCreado":post,"form_post":miFormulario,'avatar':img(request)})    
            
            
    else:
        miFormulario = formularioPost()

        return render(request, 'FECODER_APP/post/formularioPosts.html', {"form_post":miFormulario,'avatar':img(request)})

def formularioContactos(request):
    
    if request.method == 'POST':

        miFormulario = formularioContacto(request.POST)
        print("error")
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            contacto = Contacto(nombre_contacto = informacion['nombre_contacto'], celular_contacto =informacion['celular_contacto'] ,correo_contacto=informacion['correo_contacto'], mensaje=informacion['mensaje'])
            contacto.save()

            miFormulario = formularioContacto()

            return render(request, 'FECODER_APP/inicio.html', {"contactoCreado":contacto,"formularioContacto":miFormulario,'todos_post':todosPost(),'first_post':primerPost(''),'avatar':img(request)})    
          
    else:
        miFormulario = formularioContacto()

        return render(request, 'FECODER_APP/inicio.html', {"formularioContacto":miFormulario,'todos_post':todosPost(),'first_post':primerPost(''),'avatar':img(request)})

#Buscar


def buscandoPost(request):
    post=request.GET['titulo']
    todos_post=todosPost()
    primer_post=primerPost(post)
    if post!="":
        obj = Post.objects.filter(estatus_post=True).filter(titulo_post__icontains=post).first()
        
        if obj: 
            return render(request, 'FECODER_APP/inicio.html',{'post':obj,'titulo':post,'todos_post':todos_post,'first_post':obj,'formularioContacto':formularioContacto(),'avatar':img(request)})

        return render(request, 'FECODER_APP/inicio.html',{'x':"No existe post con el nombre "+post,'todos_post':todos_post,'first_post':primer_post,'formularioContacto':formularioContacto(),'avatar':img(request)})
    else:
         return render(request, 'FECODER_APP/inicio.html',{"error":"No se ingreso un nombre de post",'todos_post':todos_post,'first_post':primer_post,'formularioContacto':formularioContacto(),'avatar':img(request)})

def buscarPost(request):
         return render(request, 'FECODER_APP/inicio.html',{'avatar':img(request)})


@login_required
def buscandoContacto(request):
    nombre=request.GET['nombre']
    if nombre!="":
        obj = Contacto.objects.filter(nombre_contacto__icontains=nombre)
        if obj: 
            return render(request, 'FECODER_APP/buscarContacto.html',{'contacto':obj,'nombre':nombre,'avatar':img(request)})
   
        return render(request, 'FECODER_APP/buscarContacto.html',{'x':"No existe contacto con el nombre "+nombre,'avatar':img(request)})
    else:
         return render(request, 'FECODER_APP/buscarContacto.html',{"errorContacto":"No se ingreso un nombre de contacto",'avatar':img(request)})
         
def buscarContacto(request):
         return render(request, 'FECODER_APP/buscarContacto.html',{'avatar':img(request)})


#Usuarios
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
                return render(request, 'FECODER_APP/inicio.html',{'todos_post':todos_post,'first_post':primer_post,'formularioContacto':formularioContacto(),'avatar':img(request)})
                             
        else:
            return render(request, 'FECODER_APP/usuario/login.html',{'form_login':form,'mensaje':f"Usuario o contraseña incorrectos"})
        
    else:
        form = LoginForm()
        return render(request, 'FECODER_APP/usuario/login.html', {'form_login': form})

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
            return render(request, 'FECODER_APP/usuario/login.html',{'mensaje_login':f"Usuario registrado correctamente {username}"})
        
        return render(request, 'FECODER_APP/usuario/registro.html',{'form_register':form,'error':form.errors})

    else:
        form = RegisterForm()
        return render(request, 'FECODER_APP/usuario/registro.html', {'form_register': form})

def logoutUser(request):
    todos_post=todosPost()
    primer_post=primerPost('')
    logout(request)
    return render(request, 'FECODER_APP/inicio.html',{'todos_post':todos_post,'first_post': primer_post, 'formularioContacto':formularioContacto()})

@login_required
def editandoUsuario(request,id):
    user = User.objects.filter(id=id).first()
    if request.method == 'POST':
        form = editarUsuario(request.POST,request.FILES)
        check = request.POST.get("avatar-clear", None)
        if form.is_valid():
            user.username=form.cleaned_data['username']
            user.email=form.cleaned_data['email']
            if form.cleaned_data['first_name']:
                user.first_name=form.cleaned_data['first_name']
            if form.cleaned_data['last_name']:
                user.last_name=form.cleaned_data['last_name']
            
            user.save()
            if form.cleaned_data['avatar']:
                avatar = Avatar.objects.get(user=user)
                avatar.imagen = form.cleaned_data['avatar']
                avatar.imagen.name=user.username+".png"
                avatar.save()
            else:
                if check:
                    avatar = Avatar.objects.get(user=user)
                    avatar.imagen = 'avatars/default.png'
                    avatar.name=user.username+".png"
                    avatar.save()
               
            
            return render(request, 'FECODER_APP/inicio.html',{'todos_post':todosPost(),'first_post':primerPost(''),'formularioContacto':formularioContacto(),'avatar':img(request)})
        

    else:
        avatar=Avatar.objects.get(user=user.id)
        form = editarUsuario(initial={'username':user.username,'email':user.email,'avatar':avatar.imagen,'first_name':user.first_name,'last_name':  user.last_name})
        return render(request, 'FECODER_APP/usuario/editarPerfil.html', {'form_editar': form,'avatar':img(request),'user':user})

@login_required
def cambiarContraseña(request):
    user = request.user
    if request.method == 'POST':
        form = editarContraseña(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            
            return render(request, 'FECODER_APP/usuario/login.html')
        
        

    else:
        form = editarContraseña(request.user)
        return render(request, 'FECODER_APP/usuario/cambiarContraseña.html', {'form_cambiarContraseña': form,'avatar':img(request),})

def verPost(request,id):
   
    post=Post.objects.get(id=id)
    avatar = Avatar.objects.filter(user = post.usuario_post)  
    
    if request.method == 'POST':
        form = formularioComentario(request.POST,request.user)
        
        if form.is_valid():
            
            new_comentario = Comentario(post_comentario=post,usuario_comentario=request.user,comentario=form.cleaned_data['comentario'],fecha_comentario=datetime.now())
            new_comentario.save()
            comentario = Comentario.objects.filter(post_comentario = post)
            comentarioForm = formularioComentario()
            return render(request, 'FECODER_APP/post/mostrarPost.html',{'post':post,'img':avatar[0].imagen.url,'avatar':img(request),'comentario':comentario,'form_comentario':comentarioForm})
        
       
    else:   
        comentario = Comentario.objects.filter(post_comentario = post)
        
        form = formularioComentario(initial={'post_comentario':post,'usuario_comentario':request.user,'fecha_comentario':datetime.now(),'estatus_comentario':True})
        return render(request, 'FECODER_APP/post/mostrarPost.html',{'post':post,'img':avatar[0].imagen.url,'avatar':img(request),'comentario':comentario,'form_comentario':form})

def mostrarAvatar(id):
    user = User.objects.filter(id=id).first()
    avatar = Avatar.objects.filter(user = user)
    return avatar[0].imagen.url


@login_required
def borrarPost(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return render(request, 'FECODER_APP/inicio.html',{'todos_post':todosPost(),'first_post':primerPost(''),'formularioContacto':formularioContacto(),'avatar':img(request)})

@login_required
def editarPost(request,id):
    post=Post.objects.get(id=id)
    if request.method == 'POST':
        form = edicionPost(request.POST,request.FILES)

        if form.is_valid():
            post.titulo_post=form.cleaned_data['titulo_post']
            post.contenido_post=form.cleaned_data['contenido_post']
            post.subtitulo_post=form.cleaned_data['subtitulo_post']

            if form.cleaned_data['imagen_post']:
                post.imagen_post=form.cleaned_data['imagen_post']
            else:
                post.imagen_post=post.imagen_post

            post.save()
            return render(request, 'FECODER_APP/inicio.html',{'todos_post':todosPost(),'first_post':primerPost(''),'formularioContacto':formularioContacto(),'avatar':img(request)})
        
    else:
        form = edicionPost(initial={'titulo_post':post.titulo_post,'contenido_post':post.contenido_post,'subtitulo_post':post.subtitulo_post,'imagen_post':post.imagen_post,'estatus_post':post.estatus_post})
        return render(request, 'FECODER_APP/post/editarPost.html',{'form_post':form,'post':post,'avatar':img(request)})

@login_required
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
    return render(request, 'FECODER_APP/post/misPost.html',{'posts':posts,'img':avatar[0].imagen.url,'avatar':img(request)})


#ver todos los post al apretar en un usuario estando desde admin
def todosPostsUser(request):
    posts= Post.objects.filter(usuario_post=request.user).order_by('fecha_post')
    avatar = Avatar.objects.filter(user = request.user)
    return render(request, 'FECODER_APP/post/misPost.html',{'posts':posts,'img':avatar[0].imagen.url,'avatar':img(request)})

@login_required
def eliminarContacto(request,id):
    contacto=Contacto.objects.get(id=id)
    contacto.delete()
    return render(request, 'FECODER_APP/inicio.html',{'todos_post':todosPost(),'first_post':primerPost(''),'formularioContacto':formularioContacto(),'avatar':img(request)})

@login_required
def mostrarPerfiles(request):
    usuarios=User.objects.all()
    return render(request, 'FECODER_APP/usuario/mostrarPerfiles.html',{'perfiles':usuarios,'avatar':img(request)})

@login_required
def desactivarPerfil(request,id):
    usuario=User.objects.get(id=id)
    if usuario.is_active:
        usuario.is_active=False
        usuario.save()
    else :
        usuario.is_active=True
        usuario.save()
    usuarios=User.objects.all()
    return render(request, 'FECODER_APP/usuario/mostrarPerfiles.html',{'perfiles':usuarios,'avatar':img(request)})

@login_required
def eliminarPerfil(request,id):
    usuario=User.objects.get(id=id)
    usuario.delete()
    usuarios=User.objects.all()
    return render(request, 'FECODER_APP/usuario/mostrarPerfiles.html',{'perfiles':usuarios,'avatar':img(request)})



def verPerfil(request,id):
    usuario=User.objects.get(id=id)
    avatar = Avatar.objects.filter(user = usuario)
    posts= Post.objects.filter(usuario_post=usuario).order_by('fecha_post')
    return render(request, 'FECODER_APP/usuario/verPerfil.html',{'usuario':usuario,'img':avatar[0].imagen.url,'avatar':img(request),'posts':posts})


def comentarPost(request,post):
    if request.method == 'POST':
        form = formularioComentario(request.POST)
        if form.is_valid():
            
            return 
    else:

        form = formularioComentario()
        return render(request, 'FECODER_APP/post/comentarPost.html',{'form_comentario':form,'avatar':img(request)})








def img(request):
    img =''
    try:
        if not Avatar.objects.filter(user=request.user)[0].imagen.name=='default.jpg':
            avatar=Avatar.objects.filter(user=request.user)
            img=avatar[0].imagen.url
    except:
            img=''
    return img

def todosPost():
    if Post.objects.count()>0:
        return Post.objects.filter(estatus_post=True).order_by('contenido_post')
    else:
        return ''

def primerPost(tema):
   
    if Post.objects.all()!=None:
        if tema!='':
            if Post.objects.filter(estatus_post=True).filter(titulo_post__icontains=tema).first() :
                return Post.objects.filter(estatus_post=True).filter(titulo_post__icontains=tema).first()
            else:
                return Post.objects.filter(estatus_post=True).first()
        else:
        
            return Post.objects.filter(estatus_post=True).first()
    
