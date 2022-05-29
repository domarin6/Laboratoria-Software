from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdministradoresSerializer, AdministradoresListSerializer
from apps.base.utils import validate_files
from apps.crudRoot.models import Administrador, InfoRoot, Cliente

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
        administradores = Administrador.objects.all().values('DNI', 'nombre')
        serializer = AdministradoresListSerializer(administradores, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        data = validate_files(request.data,'imagen_de_usuario')
        serializer = AdministradoresSerializer(data = data)

        # validation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)






@api_view(['GET', 'PUT', 'DELETE'])
def administradorDetail(request, pk=None):
    #queryset
    administrador = Administrador.objects.filter(DNI=pk).first()

    #validation
    if administrador:

        # retrieve
        if request.method == 'GET':
            serializer = AdministradoresSerializer(administrador, many=False)
            return Response(serializer.data,status = status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            data = validate_files(request.data,'imagen_de_usuario', True)
            serializer = AdministradoresSerializer(administrador, data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            administrador.delete()
            return Response({'message':'El usuario ha sido eliminado satisfactoriamente!'}, status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class UserCliente(View):
    def get(self,request):
        if('listar' in request.GET):
            users=Cliente.objects.all()
            return JsonResponse(list(Cliente.values('correo','nombre')),safe=False,status=200)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)


    def post(self,request):
        if('login' in request.POST):
            if(('correo' in request.POST) and ('contrasenia' in request.POST)):
                correoRequest=request.POST['correo']
                contraseniaRequest=request.POST['contrasenia']
                user=Cliente.objects.filter(correo=correoRequest, contrasenia=contraseniaRequest)
                if(user.count()>0):
                    return JsonResponse({'Resp':True,'Rol':user.first().rol},safe=False,status=200)
                else:
                    return JsonResponse({'Resp':False},safe=False,status=200)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)


        elif('create' in request.POST):
            if(('id' in request.POST) and 
                ('name' in request.POST) and 
                ('password' in request.POST)):
                try:
                    DNIRequest=request.POST['id']
                    nombreRequest=request.POST['name']
                    passwordRequest=request.POST['password']
                    apellidoRequest=request.POST['lastName']
                    usernameRequest=request.POST['username']
                    fecha_de_nacimientoRequest=request.POST['birthDate']
                    #lugar_de_nacimientoRequest=request.POST['']
                    #direccion_de_facturacionRequest=request.POST['direccion_de_facturacion']
                    generoRequest=request.POST['genre']
                    #correo_electronicoRequest=request.POST['correo_electronico']
                    #imagen_de_usuarioRequest=request.POST['imagen_de_usuario']
                except:
                    return JsonResponse({'Resp':False},safe=False,status=400)
                try:
                    newUser=Cliente.objects.create(DNI=DNIRequest,
                                                nombre=nombreRequest,
                                                apellido=apellidoRequest,
                                                username=usernameRequest,
                                                fecha_de_nacimiento=fecha_de_nacimientoRequest,
                                                #lugar_de_nacimiento=lugar_de_nacimientoRequest,
                                                #direccion_de_facturacion=direccion_de_facturacionRequest,
                                                genero=generoRequest,
                                                #correo_electronico=correo_electronicoRequest,
                                                #imagen_de_usuario=imagen_de_usuarioRequest,
                                                password=passwordRequest,
                                                 )
                    return JsonResponse({'Resp':True},safe=False,status=201)
                except:
                    return JsonResponse({'Resp':False},safe=False,status=202)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)

@api_view(['POST'])
def administradorCreate(request):
    serializer = AdministradoresSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def administradorUpdate(request, pk):
	administrador = Administrador.objects.get(DNI=pk)
	serializer = AdministradoresSerializer(instance=administrador, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def administradorDelete(request, pk):
	administrador = Administrador.objects.get(DNI=pk)
	administrador.delete()

	return Response('Item succsesfully delete!')
