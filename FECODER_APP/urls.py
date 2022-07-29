from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name = "inicio"),
    
    path('formularioPosts', formularioPosts, name = "formularioPosts"),
    path('formularioContactos', formularioContactos, name="formularioContactos"),
    path('buscarPost', buscarPost, name="buscarPost"),
    path('buscandoPost', buscandoPost, name="buscandoPost"),
    path('buscarContacto', buscarContacto, name="buscarContacto"),
    path('buscandoContacto', buscandoContacto, name="buscandoContacto"),

    path('login', loginUser, name="login"),
    path('registro', registroUser, name="registro"),
    path('logout', logoutUser,name='logout'),


    path('password_reset_form/', auth_views.PasswordResetView.as_view(template_name='FECODER_APP/registration/password_reset_formulario.html'), name="password_reset_form"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='FECODER_APP/registration/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='FECODER_APP/registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='FECODER_APP/registration/password_reset_complete.html'), name="password_reset_complete"),
    
]