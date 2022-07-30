from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator


class Post(models.Model):

    usuario_post=models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_post = models.CharField(max_length = 30)
    subtitulo_post = models.CharField(max_length = 30)
    fecha_post = models.DateField()
    contenido_post = RichTextField(blank=True, null=True) 
    estatus_post = models.BooleanField(blank=True, default=True)
    imagen_post = models.ImageField(upload_to='post_imagenes/', null=True)

    def __str__(self):
        return self.titulo_post


class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=50)
    celular_contacto = models.IntegerField()
    correo_contacto = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre_contacto


class Comentario(models.Model):
    usuario_comentario = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comentario = models.ForeignKey('Post', on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_comentario = models.DateField()
    estatus_comentario = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.comentario

class Avatar(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE)
   imagen = models.ImageField(default='default.jpg',validators=[FileExtensionValidator(['png', 'jpg'])],             upload_to='avatars')
   
   def __str__(self):
        return self.user.username