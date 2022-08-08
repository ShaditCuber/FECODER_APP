from django.shortcuts import render,get_object_or_404
from FECODER_APP.models import Avatar
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    #cargar avatar y todo lo demas
    return render(request, 'Chat/index.html', {'usuario':request.user ,'avatar':img(request)})


def salas(request):
    usuarios=User.objects.filter().exclude(id=request.user.id)
    return render(request, 'Chat/salas/salas.html', {'usuario':request.user ,'avatar':img(request),'usuarios':usuarios})


    


def mensaje(request,id):
    print("mensaje")
    mensaje = Mensaje(texto=request.POST['contenido'])
    
   
    
  
    mensaje.save()
    mensajes =  Mensaje()
    receptor = get_object_or_404(User, id=id)
    msg= mensajes.get_mensajes(request.user,receptor)
    print(mensajes)
    
    
        
    return render(request, 'Chat/salas/sala.html', {'usuario':request.user ,'avatar':img(request),'mensajes':msg,'sala':sala})









def img(request):
    img =''
    try:
        if not Avatar.objects.filter(user=request.user)[0].imagen.name=='default.jpg':
            avatar=Avatar.objects.filter(user=request.user)
            img=avatar[0].imagen.url
    except:
            img=''
    return img