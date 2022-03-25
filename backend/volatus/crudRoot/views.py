from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdministradoresSerializer

from .models import Administradores

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

@api_view(['GET'])
def administradoresList(request):
    administradores = Administradores.objects.all()
    serializer = AdministradoresSerializer(administradores, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def administradorDetail(request, pk):
    administrador = Administradores.objects.get(id=pk)
    serializer = AdministradoresSerializer(administrador, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def administradorCreate(request):
	serializer = AdministradoresSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def administradorUpdate(request, pk):
	administrador = Administradores.objects.get(id=pk)
	serializer = AdministradoresSerializer(instance=administrador, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def administradorDelete(request, pk):
	administrador = Administradores.objects.get(id=pk)
	administrador.delete()

	return Response('Item succsesfully delete!')
