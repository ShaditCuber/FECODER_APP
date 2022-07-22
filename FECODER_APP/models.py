from tokenize import blank_re
from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length = 10)
    clave_usuario = models.CharField(max_length = 8)
    clave_verificar_usuario = models.CharField(max_length = 8, default="")
    correo_usuario = models.EmailField()

    def __str__(self):
        return self.nombre_usuario

class Post(models.Model):

    titulo_post = models.CharField(max_length = 30)
    fecha_post = models.DateField()
    contenido_post = models.TextField()
    estatus_post = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.titulo_post


class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=50)
    celular_contacto = models.IntegerField()
    correo_contacto = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre_contacto