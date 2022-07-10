from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "FECODER_APP/inicio.html")

def usuarios(request):
    return render(request, "FECODER_APP/usuarios.html")

def posts(request):
    return render(request, "FECODER_APP/posts.html")

def categorias(request):
    return render(request, "FECODER_APP/categorias.html")
