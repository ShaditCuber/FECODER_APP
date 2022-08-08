from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='padre'),
    path('salas/', salas, name='salas'),
    path('mensaje/<id>', mensaje, name='mensaje'),
 ]
