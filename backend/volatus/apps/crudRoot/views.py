from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdministradoresSerializer, AdministradoresListSerializer

from apps.crudRoot.models import Usuario, InfoRoot

#/*@api_view(['GET'])
#def RootDetail(request):
#    root = InfoRoot.objects.all()
#    serializer =
#
# Create your views here.
@api_view(['GET'])
def crudRootView(request):
    api_urls = {
		'List':'/administradores-list/',
		'Detail View':'/administradores-detail/<str:pk>/',
		'Create':'/administradores-create/',
		'Update':'/administradores-update/<str:pk>/',
		'Delete':'/administradores-delete/<str:pk>/',
		}

    return Response(api_urls)

@api_view(['GET', 'POST'])
def administradoresList(request):

    # list
    if request.method == 'GET':

        # queryset
        administradores = Usuario.objects.all().values('DNI', 'nombre')
        serializer = AdministradoresListSerializer(administradores, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        serializer = AdministradoresSerializer(data = request.data)

        # validation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)






@api_view(['GET', 'PUT', 'DELETE'])
def administradorDetail(request, pk=None):
    #queryset
    administrador = Usuario.objects.filter(id=pk).first()

    #validation
    if administrador:

        # retrieve
        if request.method == 'GET':
            serializer = AdministradoresSerializer(administrador, many=False)
            return Response(serializer.data,status = status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            serializer = AdministradoresSerializer(administrador, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            administrador.delete()
            return Response({'message':'Item succsesfully delete!'}, status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def administradorCreate(request):
	serializer = AdministradoresSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def administradorUpdate(request, pk):
	administrador = Usuario.objects.get(id=pk)
	serializer = AdministradoresSerializer(instance=administrador, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def administradorDelete(request, pk):
	administrador = Usuario.objects.get(id=pk)
	administrador.delete()

	return Response('Item succsesfully delete!')
