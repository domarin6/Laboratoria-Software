from rest_framework import serializers
from apps.flights.models import CategoryFlight

class CategoryFlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryFlight
        exclude = ('state','created_date','modified_date','deleted_date')