
from datetime import timedelta
from django.db import models

# Create your models here.
class Vuelos (models.Model):
    tipo_vuelo      =   models.CharField(max_length=20, null=False)
    fecha_vuelo     =   models.DateTimeField(null=False)
    origen          =   models.CharField(max_length=20, null=False)
    destino         =   models.CharField(max_length=20, null=False)
    tiempo_Vuelo    =   models.TimeField(null=False)
    fecha_llegada   =   models.DateTimeField(null=False)
    costo           =   models.FloatField(null=False)
    capacidad       =   models.IntegerField(null=False)

    #Define si el vuelos tiene una promocion o no.
    # 0-> vuelos sin promocion.
    # 1-> vuelos con promocion
    estado          =   models.BooleanField(default=0)

    def validDate(self, oldDate):
        """
        Si la fecha ingresada por el usuario es null, 
        entonces se asigna la fultima fecha ingresada.
        """
        if self.fecha_vuelo is None:
            self.fecha_vuelo = oldDate


    def addFechaLLegada(self):

        """
        Para obtener la fecha de llegada, se suma la fecha actual
        y el tiempo de vuelo
        """
        hour=self.tiempo_Vuelo.hour
        minute=self.tiempo_Vuelo.minute
        delta=timedelta(hours=hour, minutes=minute)
        self.fecha_llegada=self.fecha_vuelo+delta

    def asientos(self):

        """
        Se define la cantida de asietons del tipo de vuelo
        """
        if self.tipo_vuelo=='internacional':
            self.capacidad=250
        else:
            self.capacidad=150

    def setPromocion(self, oldPrice):

        """
        Si el precio ingresado es menor al precio anterior
        Se cambia el estado indicando que se aplico una promocion.
        """
        if oldPrice > self.costo:
            self.estado=True
        else:
            self.estado=False
          
    def str(self):
        print("""Tipo de vuelo {}\n
        Fecha de vuelo {}\n
        Origen {}\n
        Destino {}\n
        fecha_llegada {}""".format(self.tipo_vuelo, self.fecha_vuelo, self.origen, self.destino, self.fecha_llegada))
    
    def subCapacidad(self):
        self.capacidad-=1
