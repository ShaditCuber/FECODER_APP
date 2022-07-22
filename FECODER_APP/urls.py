from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('formularioUsuarios', formularioUsuarios, name = "formularioUsuarios"),
    path('formularioPosts', formularioPosts, name = "formularioPosts"),
    path('formularioContactos', formularioContactos, name="formularioContactos"),
    path('buscarUsuario', buscarUsuario, name="buscarUsuario"),
    path('buscandoUsuario', buscandoUsuario, name="buscandoUsuario"),
    path('buscarPost', buscarPost, name="buscarPost"),
    path('buscandoPost', buscandoPost, name="buscandoPost"),
    path('buscarContacto', buscarContacto, name="buscarContacto"),
    path('buscandoContacto', buscandoContacto, name="buscandoContacto"),
    path('login', loginUser, name="login"),
    path('registro', registroUser, name="registro"),
    
]