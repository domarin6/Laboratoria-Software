from rest_framework import serializers
from apps.tickets.models import Card, Wallet

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = ('state','created_date','modified_date','deleted_date')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = ('state','created_date','modified_date','deleted_date')
