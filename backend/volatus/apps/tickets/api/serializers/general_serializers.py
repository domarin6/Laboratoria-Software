from rest_framework import serializers

from apps.tickets.models import OrderItem
from apps.tickets.models import *
from apps.flights.api.serializers.flight_serializers import FlightSerializer

class CartFlightSerializer(serializers.ModelSerializer):

    vuelo = FlightSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['vuelo', 'cliente', 'precio', 'cantidad']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        exclude = ('state','created_date','modified_date','deleted_date')



