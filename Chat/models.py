from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

    
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='emisor', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_mensaje = models.DateTimeField(default=timezone.now)
    texto=models.TextField(max_length=500)
    visto = models.BooleanField(default=False)
    

    def __str__(self):
        return self.emisor.username + " - " + self.receptor.username + " - " + self.texto
    
    def get_mensajes(self,emisor,receptor):
        msg = list()
        m_emisor = Mensaje.objects.filter(emisor=emisor,receptor=receptor)
        m_recetor = Mensaje.objects.filter(emisor=receptor,receptor=emisor)
        for m in m_emisor:
            msg.append(m)
        for m in m_recetor:
            if m.visto == False:
                m.visto = True
                m.save()
            msg.append(m)

        lista =  sorted(msg, key=lambda x: x.fecha_mensaje)

        json = []

        for ms in lista :
            if ms.emisor == emisor:
                a=[0,ms.texto,self.format_date(ms.fecha_mensaje)]
            else:
                a=[1,ms.texto,self.format_date(ms.fecha_mensaje)]
            json.append(a)
        return json

    
    def format_date(self, data):
        return self.less_than_10(data.day) + "/" + self.less_than_10(data.month) + "/" + str(data.year) + " at " + self.less_than_10(data.hour) + ":" + self.less_than_10(data.minute) + ":" + self.less_than_10(data.second)


    def less_than_10(self, n):
        if n < 10:
	        return "0"+ str(n)
        return str(n)