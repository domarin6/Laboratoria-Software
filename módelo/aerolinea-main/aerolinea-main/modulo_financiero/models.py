from django.db import models
from django.db.models.base import ModelState
from gestion_usuarios.models import Clientes

# Create your models here.

class BasicData(models.Model):
    # se debe validar que el numero de la tarjeta sea exactamente 16 numeros
    numero      = models.CharField(max_length=16, unique=True)
    cliente     = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nombre      = models.CharField(max_length=20, null=False)
    apellido    = models.CharField(max_length=20, null=False)
    direccion   = models.CharField(max_length= 50, null=False)
    class Meta:
        abstract = True

class TarjetaDebito(BasicData):
    saldo   = models.FloatField(default=0)

    def add_saldo(self, dinero):
        try:
            self.saldo = self.saldo + dinero
            return True
        except:
            return False



class TarjetaCredito(BasicData):
    cupo    = models.FloatField(default=0)
    # se debe validar que el numero cvv sea exactamente 3 numeros
    cvv     = models.IntegerField(null=False)

    def add_cupo(self, dinero):
        try:
            self.cupo = self.cupo + dinero
            return True
        except:
            return False