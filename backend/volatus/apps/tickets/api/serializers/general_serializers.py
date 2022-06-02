from rest_framework import serializers
from apps.tickets.models import OrderItem
from apps.tickets.models import *

class CartFlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        exclude = ('state','created_date','modified_date','deleted_date')

    def to_representation(self,instance):
        return {
            'precio':instance.precio,
            'cantidad':instance.cantidad,
            'clase':instance.clase,
            'silla':instance.silla,
            'cliente':instance.cliente,
            'destino': instance.vuelo.destino,
            'fecha': instance.vuelo.fecha,
            'hora': instance.vuelo.hora,
            'tiempo_vuelo': instance.vuelo.tiempo_vuelo,
            'hora_llegada': instance.vuelo.hora_llegada,
            'costo_economico': instance.vuelo.costo_economico,
            'costo_primera_clase': instance.vuelo.costo_primera_clase,
            'image': instance.vuelo.image.url if instance.vuelo.image != '' else ''   
        }

class ShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        exclude = ('state','created_date','modified_date','deleted_date')
        

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        exclude = ('state','created_date','modified_date','deleted_date')



