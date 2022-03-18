from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Administradores (models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE)
    DNI                 =   models.IntegerField(unique=True, blank=True)
    genero              =   models.CharField(max_length=1, null=True, blank=True)
    fecha_nacimiento    =   models.DateField(null=True, blank=True)
    lugar_nacimiento    =   models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        permissions=[('admin_user', 'Usuario administrador')]
        
    def __str__(self):
        return self.user.username
    

    

class Clientes (models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE)
    DNI                 =   models.IntegerField(unique=True)
    genero              =   models.CharField(max_length=1, null=False)
    fecha_nacimiento    =   models.DateField(null=False)
    lugar_nacimiento    =   models.CharField(max_length=50, null=False)
    direccion           =   models.CharField(max_length=150, null=False)
    suscripcion         =   models.BooleanField(default=0)

    class Meta:
        permissions=[('cliente_user', 'Usuario Cliente')]

    def __str__(self):
        return self.user.username
