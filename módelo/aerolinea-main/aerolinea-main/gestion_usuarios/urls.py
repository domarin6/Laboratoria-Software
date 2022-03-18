from django.contrib import admin
from django.urls import path, include, re_path, reverse
from gestion_usuarios.views import *
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name='gestion_usuarios'
urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('noticias/', noticias, name='noticias'),
    path('login/', log_vista, name='log_vista'),
    path('suscribir/',suscribir,name="suscribir"),
    path('desuscribir/',desuscribir,name="desuscribir"),
    path('logout/', logout_vista, name='logout_vista'),
    path('registro/', registro ,name='registro'),
    path('administrarPerfil/', administrarPerfil , name='administrarPerfil'),
    path('modificar/',modificarPerfil,name='modificarPerfil'),
    path('modificado/', modificacion , name='modificacion'),
    path('eliminar/', eliminarUsuario, name='eliminarPerfil'),
    path('contraseña/nueva', PasswordResetView.as_view(template_name='gestion_usuarios/reset_email.html', email_template_name="gestion_usuarios/email.html", success_url='enviado'), name = 'password_reset'),
    path('contraseña/enviado', PasswordResetDoneView.as_view(template_name='gestion_usuarios/correo_enviado.html'), name = 'enviado'),
    re_path(r'^contraseña/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='gestion_usuarios/nueva_contraseña.html',success_url='exitosa'), name = 'password_reset_confirm'),
    path('contraseña/exitosa',PasswordResetCompleteView.as_view(template_name='gestion_usuarios/nueva_contraseña_exitosa.html') , name = 'exitosa'),
]