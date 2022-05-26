from apps.base.models import BaseModel

from django.db import models
from apps.crudRoot.models import Cliente
from apps.flights.models import Flight


class OrderItem(BaseModel):
    cliente = models.ForeignKey(Cliente, related_name='cliente',on_delete=models.CASCADE, verbose_name='Cliente', null=False)
    vuelo = models.ManyToManyField(Flight, related_name='items', verbose_name='items', null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveBigIntegerField(default=1)
    

    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = 'Orden de compra'
        verbose_name_plural = 'Ordenes de compra'

    def __str__(self):
        """Unicode representation of OrderItem."""
        return str(self.id)

class Order(BaseModel):
    pedido = models.ForeignKey(OrderItem, related_name='order_item', on_delete=models.CASCADE, verbose_name='Pedido', null=False)
    DNI = models.CharField('Identificación', unique = True, max_length=11)
    nombre = models.CharField('Nombres',max_length=100, blank = False, null = False)
    apellido = models.CharField('Apellidos',max_length=100, blank = False, null = False)
    fecha_de_nacimiento = models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False, blank = False, null = True)
    genero = models.CharField('Género',max_length=20, blank = False, null = True)
    correo_electronico = models.EmailField(blank = False, null = True)
    telefono = models.CharField('Telefono', max_length=13, blank = False, null = True)
    nombre_contacto = models.CharField('Nombre de Contacto', max_length=50, blank = False, null = True)
    telefono_contacto = models.CharField('Telefono de Contacto', max_length=13, blank = False, null = True)
    tipo = models.CharField('Compra o reserva', max_length=13, blank = False, null = True)
    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        """Unicode representation of Order"""
        return self.nombre

