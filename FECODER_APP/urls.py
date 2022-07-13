from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name = "Inicio"),
    #path('usuarios', views.usuarios, name = "Usuarios"),
    path('posts', posts, name = "Posts"),
    path('categorias', categorias, name = "Categorias"),
    path('formularioUsuarios', formularioUsuarios, name = "formularioUsuarios"),
    path('formularioPosts', formularioPosts, name = "formularioPosts"),
    path('formularioCategorias', formularioCategorias, name = "formularioCategorias"),
    path('formularioComentarios', formularioComentarios, name="formularioComentarios"),
    path('buscarUsuario', buscarUsuario, name="buscarUsuario"),
    path('buscarUsuariox', buscarUsuariox, name="buscarUsuariox"),
    path('buscarPost', buscarPost, name="buscarPost"),
    path('buscarPostx', buscarPostx, name="buscarPostx"),
]