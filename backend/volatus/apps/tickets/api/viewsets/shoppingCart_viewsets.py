from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.flights.models import Flight
from apps.tickets.models import Order, OrderItem, ShoppingCart

from apps.tickets.api.serializers.general_serializers import CartFlightSerializer, OrderSerializer,  ShoppingCartSerializer

class shoppingCartViewSet(viewsets.GenericViewSet):

    @action(methods=['post'], detail=False)
    def add_flight(self,request):
        ordersTotal = OrderItem.objects.filter(cliente=request.data['cliente']).filter(vuelo=request.data['vuelo']).first()
        flight = Flight.objects.filter(id=request.data['vuelo']).first()
        idCliente = request.data['cliente']
        shoppingCartCreate = ShoppingCart.objects.filter(cliente=idCliente).first()
        if shoppingCartCreate:
            cantidadTotal = shoppingCartCreate.cantidadOrders + request.data['cantidad']
            if cantidadTotal > 5:
                return Response({'Error':'No se puede agregar mas de cinco vuelos al carrito!'}, status=status.HTTP_400_BAD_REQUEST)

        if ordersTotal:
            cantidad = ordersTotal.cantidad + request.data['cantidad']
            precio = cantidad*flight.costo
            vuelo = request.data['vuelo']
            data_Order = {
                "cliente": idCliente,
                "vuelo": vuelo,
                "cantidad": cantidad,
                "precio": precio
            }
            serializerOrder = CartFlightSerializer(ordersTotal, data=data_Order)
            if serializerOrder.is_valid():
                serializerOrder.save()
            else:
                return Response({'message':'', 'error':serializerOrder.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            idCliente = request.data['cliente']
            cantidad =  request.data['cantidad']
            precio = flight.costo*cantidad
            vuelo = request.data['vuelo']
            data_Order = {
                "cliente": idCliente,
                "vuelo": vuelo,
                "cantidad": cantidad,
                "precio": precio
            }
            serializerOrder = OrderSerializer(data=data_Order)
            if serializerOrder.is_valid():
                serializerOrder.save()
            else:
                return Response({'message':'', 'error':serializerOrder.errors}, status=status.HTTP_400_BAD_REQUEST)

        if shoppingCartCreate:   
            precioTotal = cantidadTotal*flight.costo
            dataCart = {
                'orders': ordersTotal.id,
                "cliente": idCliente,
                "vuelo": vuelo,
                "cantidadOrders": cantidadTotal,
                "precioTotal": precioTotal
            }
            serializerShoppingCart = ShoppingCartSerializer(shoppingCartCreate, data=dataCart)
            if serializerShoppingCart.is_valid():
                serializerShoppingCart.save()
                return Response({'message': 'Vuelo agregado correctamente al carrito!'}, status=status.HTTP_201_CREATED)

            else:
                return Response({'message':'', 'error':serializerShoppingCart.errors}, status=status.HTTP_400_BAD_REQUEST)

        else:
            dataCart = {
                "Orders": ordersTotal.id,
                "cliente": idCliente,
                "vuelo": vuelo,
                "cantidadOrders": cantidad,
                "precioTotal": precio
            }
            serializerShoppingCart = ShoppingCartSerializer(data=dataCart)
            if serializerShoppingCart.is_valid():
                serializerShoppingCart.save()
                return Response({'message': 'Vuelo agregado correctamente al carrito!'}, status=status.HTTP_201_CREATED)      
            else:
                return Response({'message':'', 'error':serializerShoppingCart.errors}, status=status.HTTP_400_BAD_REQUEST)


       
    @action(methods=['get'], detail=False)
    def get_flights(self,request):
        data_shoppingCart = ShoppingCart.objects.filter(cliente=request.data['cliente']).first()
        if data_shoppingCart:
            ordersFlight = OrderItem.objects.filter(state=True).filter(cliente=request.data['cliente'])
            ordersFlightSerializer = CartFlightSerializer(instance=ordersFlight, many=True)
            return Response(ordersFlightSerializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'vacio':'No se han agregado vuelos al carrito!'}, status=status.HTTP_400_BAD_REQUEST)

            

    @action(methods=['delete'], detail=False)
    def delete_flight(self,request):
        data_Order = OrderItem.objects.filter(cliente=request.data['cliente']).filter(vuelo=request.data['vuelo']).first()
        cantidad = request.data['cantidad']
        precio = data_Order.precio
        data_shoppingCart = ShoppingCart.objects.filter(cliente=request.data['cliente']).first()
        if data_shoppingCart and data_Order:
            cantidadTotal = data_shoppingCart.cantidadOrders - cantidad
            precioTotal = data_shoppingCart.precioTotal - precio
            cantidadOrder = data_Order.cantidad - cantidad
            precioOrder = data_Order.precio - precio
            completeDataCart = {
                "orders": data_Order.id,
                "cliente": request.data['cliente'],
                "vuelo": request.data['vuelo'],
                "cantidadOrders": cantidadTotal,
                "precioTotal": precioTotal
            }
            completedataOrder = {
                "cliente": request.data['cliente'],
                "vuelo": request.data['vuelo'],
                "cantidad": cantidadOrder,
                "precio": precioOrder
            }
            serializerOrder = CartFlightSerializer(data_Order, data=completedataOrder)
            if serializerOrder.is_valid():
                serializerOrder.save()
            else:
                return Response({'message':'', 'error':serializerOrder.errors}, status=status.HTTP_400_BAD_REQUEST)

            serializerShoppingCart = ShoppingCartSerializer(data_shoppingCart, data=completeDataCart)
            if serializerShoppingCart.is_valid():
                serializerShoppingCart.save()
                return Response({'message': 'Vuelo eliminado correctamente del carrito!'}, status=status.HTTP_200_OK)
            else:
                return Response({'message':'', 'error':serializerShoppingCart.errors}, status=status.HTTP_400_BAD_REQUEST)      
        else:
            return Response({'Vacío':'No se ha agregado el vuelo al carrito!'}, status=status.HTTP_400_BAD_REQUEST)
        


    
    

    
