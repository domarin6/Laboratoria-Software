from rest_framework import serializers
from apps.crudRoot.models import Usuario, InfoRoot

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('DNI', 'username', 'nombre')

class AdministradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        administrador = Usuario(**validated_data)
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
        model = Usuario

    def to_representation(self, instance):
        return {
            'DNI': instance['DNI'],
            'nombre': instance['nombre']
        }

class InfoRootSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoRoot
        fields = '__all__'
