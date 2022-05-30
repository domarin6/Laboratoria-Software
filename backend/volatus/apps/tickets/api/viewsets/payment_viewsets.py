from functools import reduce
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.tickets.models import Wallet, Card
from apps.tickets.api.serializers.payment_serializers import CardSerializer, WalletSerializer

class CardViewset(viewsets.GenericViewSet):
    def numbers(self, number):
        return len(list(filter(lambda x:ord(x)<48 or ord(x)>57,number)))==0 and len(number)==16

    @action(methods=['post'], detail=False)
    def add_card(self,request):
        dic={3:'American Express',4:'VISA',5:'MasterCard',6:'Discover'}
        code=request.data['number']
        if self.numbers(code)==True:
            if int(code[0]) in dic:
                tipo=dic[int(code[0])]
                sm= reduce(lambda x,y:x+y,map(lambda x:x%2==0 and int(code[x])*2%9 or int(code[x]),range(len(code))))
                if sm%10==0 and sm<=150:
                    if tipo=='American Express':
                        cvv2=code[5]+code[7]+code[11]+(code[2]!='9' and str(int(code[2])+1) or '1')
                    else:
                        cvv2=code[7]+code[11]+(code[2]!='9' and str(int(code[2])+1) or '1')
                    serializer = CardSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data,status = status.HTTP_201_CREATED)
                    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'Error':'Tarjeta no valida.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error':'Tipo de tarjeta no reconocido.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def get_cards(self,request):
        data_cards = Card.objects.filter(idCliente=request.data['cliente'])
        if data_cards:
            serializer = CardSerializer(data_cards, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({'message':'No se ha encontrado tarjetas'}, status = status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def get_card(self,request, pk=None):
        card = Card.objects.filter(id=pk).first()
        if card:
            serializer = CardSerializer(card, many=False)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({'message':'No se ha encontrado una tarjeta con esos datos'}, status = status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=True)
    def delete_card(self,request, pk=None):
        card = Card.objects.filter(id=pk).first()
        if card:
            card.delete()
            return Response({'message':'La tarjeta ha sido eliminada satisfactoriamente!'}, status = status.HTTP_200_OK)
        return Response({'message':'No se ha encontrado una tarjeta con estos datos'}, status = status.HTTP_400_BAD_REQUEST)



class WalletViewSet(viewsets.GenericViewSet):
    
    @action(methods=['post'], detail=False)
    def add_cash(self,request):
        wallet = Wallet.objects.filter(idcliente=request.data['idcliente']).first()
        if wallet:
            cash = Wallet.cash + request.data['cash']
            idCliente = Wallet.idCliente
            dataWallet={
                "cash": cash,
                "idcliente": idCliente
            }
            serializer = WalletSerializer(wallet, data=dataWallet)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
