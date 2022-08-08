from django.shortcuts import render,get_object_or_404
from FECODER_APP.models import Avatar
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    #cargar avatar y todo lo demas
    return render(request, 'Chat/index.html', {'usuario':request.user ,'avatar':img(request)})


def salas(request):
    usuarios=User.objects.filter().exclude(id=request.user.id)
    return render(request, 'Chat/salas/salas.html', {'usuario':request.user ,'avatar':img(request),'usuarios':usuarios})


def crearSala(request,id):
    sala = Mensaje(emisor=request.user,receptor=get_object_or_404(User,id=id))
    sala.save()
    form = MensajeForm()
    return render(request, 'Chat/salas/sala.html', {'usuario':request.user ,'avatar':img(request),'receptor':sala.receptor,'formMensaje':form})


def enviarMensaje(request,receptor):
    
    print(receptor)
    if request.method == 'POST':
        
        
            
            uwu= Mensaje.objects.filter(emisor=request.user,receptor=get_object_or_404(User,username=receptor)).update(texto=request.POST['contenido'])
            
            instancia=Mensaje()
            mensajes = instancia.get_mensajes(request.user,get_object_or_404(User,username=receptor))
            print(mensajes)
            return render(request, 'Chat/salas/sala.html', {'usuario':request.user ,'avatar':img(request),'receptor':receptor,'mensajes':mensajes})
    else:
        form = MensajeForm()
        return render(request, 'Chat/salas/sala.html', {'usuario':request.user ,'avatar':img(request),'formMensaje':form})








def img(request):
    img =''
    try:
        if not Avatar.objects.filter(user=request.user)[0].imagen.name=='default.jpg':
            avatar=Avatar.objects.filter(user=request.user)
            img=avatar[0].imagen.url
    except:
            img=''
    return img