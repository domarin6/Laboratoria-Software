from time import strptime
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from datetime import datetime, date, time, timedelta

from apps.base.utils import validate_files
from apps.flights.api.serializers.flight_serializers import (
    FlightSerializer, FlightRetrieveSerializer
)

class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    parser_classes = (JSONParser, MultiPartParser, )
    dict_vuelo = {
            "bogota": {"pereira":[44,0],
                            "bogota":[0,0],
                            "medellin":[48,0],
                            "cali":[52,0],
                            "cartagena":[79,0],
                            "miami":[211,60],
                            "londres":[636,360],
                            "new york":[327,60],
                            "madrid":[630,420],
                            "buenos aires":[379,120]},

            "pereira": {"pereira":[0,0],
                            "bogota":[44,0],
                            "medellin":[42,0],
                            "cali":[30,0],
                            "cartagena":[79,0],
                            "miami":[211,60],
                            "londres":[636,360],
                            "new york":[327,60],
                            "madrid":[630,420],
                            "buenos aires":[379,120]},

            "medellin": {"pereira":[42,0],
                            "bogota":[48,0],
                            "medellin":[0,0],
                            "cali":[30,0],
                            "cartagena":[60,0],
                            "miami":[200,60],
                            "londres":[636,360],
                            "new york":[327,60],
                            "madrid":[630,420],
                            "buenos aires":[379,120]},

    
            "cali":{"pereira":[30,0],
                            "bogota":[52,0],
                            "medellin":[30,0],
                            "cali":[0,0],
                            "cartagena":[79,0],
                            "miami":[211,60],
                            "londres":[636,360],
                            "new york":[327,60],
                            "madrid":[630,427],
                            "buenos aires":[379,120]},

  
            "cartagena":{"pereira":[79,0],
                            "bogota":[79,0],
                            "medellin":[60,0],
                            "cali":[79,0],
                            "cartagena":[0,0],
                            "miami":[180,60],
                            "londres":[636,360],
                            "new york":[300,60],
                            "madrid":[600,427],
                            "buenos aires":[379,120]},

        }

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
        fecha = request.data['fecha']
        fecha = datetime.strptime(fecha, '%Y-%m-%d')
        hora = request.data['hora']
        hora = datetime.strptime(hora,'%H:%M:%S')
        fecha_hora = datetime(fecha.year,fecha.month,fecha.day,hora.hour,hora.minute)
        origen = request.data['origen']
        destino = request.data['destino']
        tiempo_vuelo = self.dict_vuelo[origen][destino][0]
        tiempo_vuelo = tiempo_vuelo *60
        tiempo_vuelo = timedelta(0,tiempo_vuelo,0)
        diferencia_horaria = self.dict_vuelo[origen][destino][1] * 60
        diferencia_horaria = timedelta(0,diferencia_horaria,0)
        hora_llegada = fecha_hora + tiempo_vuelo + diferencia_horaria
        data = {
            "fecha": request.data['fecha'],
            "hora":  request.data['hora'],
            "origen": request.data['origen'],
            "destino": request.data['destino'],
            "tiempo_vuelo": str(tiempo_vuelo),
            "hora_llegada": str(hora_llegada),
            "costo_economico": request.data['costo_economico'],
            "costo_primera_clase": request.data['costo_primera_clase'],
            "rating": request.data['rating'],
            "full_description": request.data['full_description'],
            "categoria": request.data['categoria'],
            "image": request.data['image']
        }
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
            fecha = request.data['fecha']
            hora = request.data['hora']
            fecha_hora = datetime(fecha.year,fecha.month,fecha.day,hora.hour,hora.second)
            origen = request.data['origen']
            destino = request.data['destino']
            tiempo_vuelo = self.dict_vuelo[origen][destino]
            tiempo_vuelo = tiempo_vuelo *60
            tiempo_vuelo = timedelta(0,tiempo_vuelo)
            hora_llegada = fecha_hora + timedelta(0,tiempo_vuelo)
            data = {
                "fecha": request.data['fecha'],
                "hora":  request.data['hora'],
                "origen": request.data['origen'],
                "destino": request.data['destino'],
                "tiempo_vuelo": tiempo_vuelo,
                "hora_llegada": hora_llegada,
                "costo_economico": request.data['costo_economico'],
                "costo_primera_clase": request.data['costo_primera_clase'],
                "rating": request.data['rating'],
                "full_description": request.data['full_description'],
                "categoria": request.data['categoria'],
                "image": request.data['image']
            }
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