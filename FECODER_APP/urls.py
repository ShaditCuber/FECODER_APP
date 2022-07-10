from django.urls import path
from FECODER_APP import views

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('usuarios', views.usuarios, name = "Usuarios"),
    path('posts', views.posts, name = "Posts"),
    path('categorias', views.categorias, name = "Categorias"),
    path('formularioUsuarios', views.formularioUsuario, name = "formularioUsuarios"),
]