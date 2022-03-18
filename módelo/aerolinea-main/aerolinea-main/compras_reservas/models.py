from django.db import models
from gestion_vuelos.models import Vuelos
from gestion_usuarios.models import Clientes
from datetime import datetime

# Create your models here.
class Viajero (models.Model):
    DNI                 =   models.IntegerField()
    genero              =   models.CharField(max_length=1, null=False)
    fecha_nacimiento    =   models.DateField(null=False)
    lugar_nacimiento    =   models.CharField(max_length=50, null=False)
    direccion           =   models.CharField(max_length=150, null=False)
    email               =   models.EmailField(null=False)
    nombre_contacto     =   models.CharField(max_length=20, null=False)
    telefono_contacto   =   models.CharField(max_length=20, null=False)
    acompañante         =   models.IntegerField(blank=True,null=True)
    silla               =   models.CharField(max_length=5, null=False)
    clase               =   models.BooleanField(null=False, default=1)
    # 0-> no ha realizado checkin.
    # 1-> realizo check-in
    check_in            =   models.BooleanField(default=0)

    def menor_edad(self):
        years_old=datetime.now().year-self.fecha_nacimiento.year
        if years_old<18:
            return True


    


# Esta es una clase abstracta, no se vera reflejada en la base de datos.
# Estos datos basicos son heredados por compras y reservas.
# Se crean tablas independientes para cada uno
class BasicData(models.Model):
    cliente         =   models.ForeignKey(Clientes, on_delete=models.CASCADE)
    viajero         =   models.OneToOneField(Viajero, on_delete=models.CASCADE)
    vuelo           =   models.ForeignKey(Vuelos, on_delete=models.CASCADE)
    estado_reserva  =   models.BooleanField(default=0)
    creacion_reserva=   models.DateTimeField()

    class Meta:
        abstract = True



class Reservas (BasicData):
    
    def __str__(self):
        return self.cliente.DNI  


class Compras (BasicData):

    def __str__(self):
        return self.cliente.DNI  