from rest_framework import serializers

from apps.flights.models import Flight
from apps.flights.api.serializers.general_serializers import (
    CategoryFlightSerializer
)

class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        exclude = ('state','created_date','modified_date','deleted_date')


    def validate_categoria(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una Categoría de Vuelo")
        return value

    def validate(self, data):
        if 'categoria' not in data.keys():
            raise serializers.ValidationError({
                "categoria": "Debe ingresar una Categoria de Vuelo."            
            })
        
        return data

    def to_representation(self,instance):
        return {
            'destino': instance.destino,
            'fecha': instance.fecha,
            'hora': instance.hora,
            'tiempo_vuelo': instance.tiempo_vuelo,
            'hora_llegada': instance.hora_llegada,
            'costo': instance.costo,
            'image': instance.image.url if instance.image != '' else ''
            
        }

class FlightRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        exclude = ('state','created_date','modified_date','deleted_date')