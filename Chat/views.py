from django.shortcuts import render,get_object_or_404
from FECODER_APP.models import Avatar
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.


def index(request):
    #cargar avatar y todo lo demas
    return render(request, 'Chat/index.html', {'usuario':request.user ,'avatar':img(request)})


def salas(request):
    usuarios=User.objects.filter().exclude(id=request.user.id)
    instancia = Mensaje()
    recientes = instancia.obtener_usuario_recientes(request.user)
    print(recientes)
    return render(request, 'Chat/salas/salas.html', {'usuario':request.user ,'avatar':img(request),'usuarios':usuarios,'recientes':recientes})


def crearSala(request,id):
    instancia=Mensaje()
    mensajes = instancia.get_mensajes(request.user,get_object_or_404(User,id=id))
    mensajes2=instancia.get_mensajes(get_object_or_404(User,id=id),request.user)
    if mensajes or mensajes2:
        return render(request, 'Chat/salas/sala.html', {'usuario':request.user ,'avatar':img(request),'mensajes':mensajes,'ip':id,'receptor':get_object_or_404(User,id=id)})

    return render(request, 'Chat/salas/sala.html', {'usuario':request.user ,'avatar':img(request),'ip':id,'receptor':get_object_or_404(User,id=id)})


def enviarMensaje(request,id):
    
    
    if request.method == 'POST' and request.POST['contenido']!='':     
            
            
            sala = Mensaje(emisor=request.user,receptor=get_object_or_404(User,id=id),texto=request.POST['contenido'],fecha_mensaje=datetime.now())
            sala.save()
            
            instancia=Mensaje()
            mensajes = instancia.get_mensajes(request.user,get_object_or_404(User,id=id))
            receptor = get_object_or_404(User,id=id)
            visto =instancia.verificar_visto_ultimo_mensaje(request.user,receptor)
        

                  
            return render(request, 'Chat/salas/sala.html', {'usuario':request.user ,'avatar':img(request),'mensajes':mensajes,'ip':id,'receptor':receptor,'visto':visto})
    else:
        instancia=Mensaje()
        mensajes = instancia.get_mensajes(request.user,get_object_or_404(User,id=id))
        return render(request, 'Chat/salas/sala.html', {'usuario':request.user ,'avatar':img(request),'mensajes':mensajes,'ip':id,'receptor':get_object_or_404(User,id=id)})








def img(request):
    img =''
    try:
        if not Avatar.objects.filter(user=request.user)[0].imagen.name=='default.jpg':
            avatar=Avatar.objects.filter(user=request.user)
            img=avatar[0].imagen.url
    except:
            img=''
    return img