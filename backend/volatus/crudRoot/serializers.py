from rest_framework import serializers
from .models import Administradores, InfoRoot

class AdministradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administradores
        fields = '__all__'

class InfoRootSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoRoot
        fields = '__all__'
