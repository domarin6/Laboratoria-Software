from rest_framework import serializers
from apps.crudRoot.models import Administrador, Usuario, InfoRoot, Cliente

from datetime import datetime


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('DNI', 'username', 'nombre')

class AdministradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        exclude = ('groups', 'user_permissions', )

    def validate_fecha_de_nacimiento(self, value):
        if ( value != None):
            today = date.today()
            try:
                birthday = value.replace(year = today.year)

            except ValueError:
                birthday = value.replace(year = today.year, month = value.month + 1, day = 1)

            if birthday > today:
                age = today.year - value.year - 1
            else:
                age = today.year - value.year

            if(age >= 18):
                return value
            else: serializers.ValidationError('El usuario es menor de edad')

        return value


    def create(self, validated_data):
        administrador = Administrador(**validated_data)
        administrador.set_password(validated_data['password'])
        administrador.save()
        return administrador

    def update(self,instance,validated_data):
        update_administrador = super().update(instance, validated_data)
        update_administrador.set_password(validated_data['password'])
        update_administrador.save()
        return update_administrador

class AdministradoresListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador

    def to_representation(self, instance):
        return {
            'DNI': instance['DNI'],
            'nombre': instance['nombre']
        }

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ('groups', 'user_permissions', )

    def create(self, validated_data):
        cliente = Cliente(**validated_data)
        cliente.set_password(validated_data['password'])
        cliente.save()
        return cliente

    def update(self,instance,validated_data):
        update_cliente = super().update(instance, validated_data)
        update_cliente.set_password(validated_data['password'])
        update_cliente.save()
        return update_cliente

class ClientesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente

    def to_representation(self, instance):
        return {
            'DNI': instance['DNI'],
            'nombre': instance['nombre']
        }
           
class InfoRootSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoRoot
        fields = '__all__'
