from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.base.utils import validate_files
from apps.flights.api.serializers.flight_serializers import (
    FlightSerializer, FlightRetrieveSerializer
)

class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    parser_classes = (JSONParser, MultiPartParser, )

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        flight_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": flight_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer 
        data = validate_files(request.data,'image')
        serializer = self.serializer_class(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Vuelo creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        flight = self.get_queryset(pk)
        if flight:
            flight_serializer = FlightRetrieveSerializer(flight)
            return Response(flight_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Vuelo con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            data = validate_files(request.data, 'image', True)
            flight_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
            if flight_serializer.is_valid():
                flight_serializer.save()
                return Response({'message':'Vuelo actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':flight_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        flight = self.get_queryset().filter(id=pk).first() # get instance        
        if flight:
            flight.state = False
            flight.save()
            return Response({'message':'Vuelo eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Vuelo con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)