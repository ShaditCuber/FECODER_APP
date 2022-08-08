from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='padre'),
    path('salas/', salas, name='salas'),
    path('enviarMensaje/<id>', enviarMensaje, name='enviarMensaje'),
    path('crearSala/<id>', crearSala, name='crearSala'),
 ]
