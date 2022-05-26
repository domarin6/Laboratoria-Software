from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.flights.models import Flight
from apps.tickets.models import Order, OrderItem

from apps.tickets.api.serializers.general_serializers import CartFlightSerializer, OrderSerializer

class shoppingCartViewSet(viewsets.GenericViewSet):

    @action(methods=['post'], detail=False)
    def add_flight(self,request):
        orderCliente = OrderItem.objects.filter(cliente=request.data['cliente']).first()
        vuelo = Flight.objects.filter(id = request.data['vuelo']).first()

        if orderCliente and vuelo:
            if orderCliente.cantidad > 5:
                return Response({'error':'No puede agregar mas de cinco vuelos'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                orderCliente.cantidad = orderCliente.cantidad + 1
                orderCliente.precio = orderCliente.precio + vuelo.costo
                orderCliente = orderCliente.vuelo.add(vuelo)
                orderCliente.save()
                return Response({'message':'Vuelo agregado correctamente al carrito!'}, status=status.HTTP_201_CREATED)

        else:
            orderCliente = CartFlightSerializer(data = request.data)
            if orderCliente.is_valid():
                orderCliente.precio = vuelo.costo
                orderCliente.save()
                return Response({'message': 'Vuelo agregado correctamente al carrito!'}, status=status.HTTP_201_CREATED)
            return Response({'message':'', 'error':orderCliente.errors}, status=status.HTTP_400_BAD_REQUEST)
        


       
    @action(methods=['get'], detail=False)
    def get_flights(self,request):
        data_Order = OrderItem.objects.filter(state=True).order_by('id')
        data = CartFlightSerializer(data_Order, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=True)
    def delete_flight(self,request, pk=None):

        orderCliente = OrderItem.objects.filter(cliente=request.data['cliente']).first()
        flight = Flight.objects.filter(id = pk).first()

        if orderCliente and flight:
            if orderCliente.cantidad == 1:
                orderCliente.state = False
                orderCliente.save()
                return Response({'message':'Vuelo eliminado correctamente al carrito!'}, status=status.HTTP_200_OK)
            else:
                orderCliente = orderCliente.vuelo.remove(flight)
                return Response({'message':'Vuelo eliminado correctamente al carrito!'}, status=status.HTTP_200_OK)
        
        return Response({'error':'No existe un Vuelo con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
        


    
    

    
