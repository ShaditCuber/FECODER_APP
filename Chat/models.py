from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

    
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='emisor', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_mensaje = models.DateTimeField(default=datetime.now)
    texto=models.TextField(max_length=500)
    visto = models.BooleanField(default=False)
    

    def __str__(self):
        return self.texto
    
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
        return self.less_than_10(data.day) + "/" + self.less_than_10(data.month) + "/" + str(data.year) + " a las  " + self.less_than_10(data.hour) + ":" + self.less_than_10(data.minute) + ":" + self.less_than_10(data.second)


    def less_than_10(self, n):
        if n<10:
            return "0" + str(n)
        
        return str(n)

      
    def verificar_visto_ultimo_mensaje(self, user_loged, user_visited):
        ultimo_mensaje = self.ultimo_mensaje(user_loged, user_visited)
        if ultimo_mensaje != False:
            if ultimo_mensaje.emisor == user_visited and ultimo_mensaje.visto:
                return True
            return True
        return False

    def ultimo_mensaje(self, user_loged, user_visited):
        ms=list()
        mlog = Mensaje.objects.filter(emisor=user_loged, receptor=user_visited)
        mvis = Mensaje.objects.filter(emisor=user_visited, receptor=user_loged)

        for m in mlog:ms.append(m)
        for m in mvis:ms.append(m)

        if len(ms)==0:return False

        return sorted(ms, key=lambda x: x.fecha_mensaje)[-1]
    
    def obtener_usuario_recientes(self, user_loged):
        l = list()
        for user_visited in User.objects.all():
            if self.ultimo_mensaje(user_loged, user_visited):
                leer = True
                if self.ultimo_mensaje(user_loged,user_visited).emisor != user_loged and self.ultimo_mensaje(user_loged,user_visited).visto == False:leer = False
                l.append([user_visited,self.ultimo_mensaje(user_loged, user_visited),leer])
        return sorted((sorted(l, key=lambda inst: inst[1].fecha_mensaje)[::-1]), key=lambda inst: inst[1].visto)


    
    
        
