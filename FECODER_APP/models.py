from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length = 10)
    clave_usuario = models.CharField(max_length = 8)
    correo_usuario = models.EmailField()

class Post(models.Model):

    titulo_post = models.CharField(max_length = 30)
    fecha_post = models.DateField()
    contenido_post = models.TextField()
    estatus_post = models.BooleanField()

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length = 15)

class Comentario(models.Model):
    comentario_post = models.CharField(max_length = 80)

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=50)
    celular_contacto = models.IntegerField()
    correo_contacto = models.EmailField()
    mensaje = models.TextField()
