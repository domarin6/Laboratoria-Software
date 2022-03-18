from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from gestion_usuarios.models import *
from gestion_usuarios import views
from django.contrib.auth.models import User
from gestion_usuarios.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.urls import reverse
from busqueda_noticias.capital import Capital
from django.utils import timezone
#list
from django.core.paginator import Paginator
from busqueda_noticias.forms import *
from gestion_usuarios.models import Clientes
from gestion_vuelos.models import *
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

ZONA = {'Madrid': 'Europe/Madrid',
            'Londres': 'Europe/London',
            'New York': 'America/New_York',
            'Buenos Aires':'America/Argentina/Buenos_Aires',
    }
# Create your views here.

def index (request):
    if request.user.is_authenticated:
        return redirect('gestion_usuarios:administrarPerfil')
    else:
        return redirect('gestion_usuarios:inicio')

def log_vista(request):
    if request.user.is_authenticated:
        return redirect('gestion_usuarios:administrarPerfil')
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gestion_usuarios:administrarPerfil')
            else:
                #return render(request,'gestion_usuarios/login.html',{'mensaje':mensaje})
                url_rev=reverse('gestion_usuarios:log_vista')+'?False'
                return redirect(url_rev)
        elif request.method=='GET':
            return render(request,'gestion_usuarios/login.html')

@login_required
def logout_vista(request):
    logout(request)
    return redirect('gestion_usuarios:logout_vista')


def registro(request):
    if request.method=='POST':
        form=FormUser(request.POST)
        form2=FormCliente(request.POST)

        if form.is_valid() and form2.is_valid():
            usuario=form.save(commit=False)
            #usuario.set_password(usuario.password)
            cliente=form2.save(commit=False)
            cliente.user=usuario

            permission = Permission.objects.get(
                codename='cliente_user',
            )

            usuario.save()
            cliente.save()

            usuario.user_permissions.add(permission)
            return redirect('gestion_usuarios:log_vista')
        else:
            print(form.errors)
            print(form2.errors)  
    elif request.method=='GET':
        form=FormUser()
        form2=FormCliente()
    
    return render(request,'gestion_usuarios/registro.html',{'form':form, 'form2':form2})

@login_required
def administrarPerfil(request):
    usuario=request.user
    if usuario.has_perm('gestion_usuarios.admin_user'):
        return render(request,'gestion_usuarios/menu_perfil_administrador.html')
    elif usuario.has_perm('gestion_usuarios.cliente_user'):
        return redirect('gestion_usuarios:noticias')
    
    
@login_required
def modificarPerfil(request):
    usuario=request.user
    #usuario=User.objects.get(id=17)
    tipo = None
    if usuario.has_perm('gestion_usuarios.admin_user'):
        admin=usuario.administradores
        form2=FormAdministrador(instance=admin)
        tipo = "administrador"
    elif usuario.has_perm('gestion_usuarios.cliente_user'):
        cliente=usuario.clientes
        form2=FormCliente(instance=cliente)
        tipo = "cliente"
    form=FormUser(instance=usuario)
    return render(request,'gestion_usuarios/modificar_perfil.html',{'form':form, 'form2':form2,"tipo":tipo})

@login_required
def modificacion(request):
    usuario=request.user
    #usuario=User.objects.get(id=17)
    if usuario.has_perm('gestion_usuarios.admin_user'):
        admin=usuario.administradores
        form2=FormAdministrador(request.POST, instance=admin)
    elif usuario.has_perm('gestion_usuarios.cliente_user'):
        cliente=usuario.clientes
        form2=FormCliente(request.POST, instance=cliente)
    form=FormUser(request.POST,instance=usuario)
    if form.is_valid() and form2.is_valid():
        form.save(commit=False)
        form2.save(commit=False)
        form.set_password=form.password
        form.save()
        form2.save()
    return redirect('gestion_usuarios:administrarPerfil')
    
@login_required
def eliminarUsuario(request):
    usuario=request.user
    logout(request)
    if usuario.has_perm('gestion_usuarios.admin_user'):
        admin=usuario.administradores
        admin.delete()
    elif usuario.has_perm('gestion_usuarios.cliente_user'):
        cliente=usuario.clientes
        cliente.delete()
    usuario.delete()
    return redirect('index')

def inicio(request):
    vuelo_imagen=list()
    capital         = Capital()

    lista_vuelos    =   Vuelos.objects.filter(fecha_vuelo__gt=timezone.localtime(timezone.now()).today(),estado = False ).order_by('fecha_vuelo')
    for vuelo in lista_vuelos:
        imagen      =   capital.url_capital(vuelo.destino)
        vuelo_imagen.append([vuelo,imagen])

    pagina          =   Paginator(vuelo_imagen, 5)

    page_number     =   request.GET.get('page', 1)
    
    page_obj        =   pagina.get_page(page_number)

    return render(request, 'gestion_usuarios/index.html', {'page_obj': page_obj, 'zona':ZONA})

@permission_required('gestion_usuarios.cliente_user')
def noticias(request):
    usuario=request.user
    cliente=Clientes.objects.get(user_id=usuario.id)

    vuelo_imagen=list()
    capital         = Capital()

    lista_vuelos    =   Vuelos.objects.filter(fecha_vuelo__gt=timezone.localtime(timezone.now()).today() ).order_by('fecha_vuelo')
    for vuelo in lista_vuelos:
        imagen      =   capital.url_capital(vuelo.destino)
        vuelo_imagen.append([vuelo,imagen])

    pagina          =   Paginator(vuelo_imagen, 5)

    page_number     =   request.GET.get('page', 1)
    
    page_obj        =   pagina.get_page(page_number)

    return render(request, 'gestion_usuarios/menu_perfil_cliente.html', {'page_obj': page_obj, 'zona':ZONA, 'suscripcion':cliente.suscripcion})

@permission_required('gestion_usuarios.cliente_user')
def suscribir(request):
    usuario=request.user
    cliente=Clientes.objects.get(user_id=usuario.id)
    try:
        cliente.suscripcion = True
        cliente.save()
        url_rev=reverse('gestion_usuarios:noticias')+'?subs'
        return redirect(url_rev)
    except:
        url_rev=reverse('gestion_usuarios:noticias')+'?non_subs'
        return redirect(url_rev)


@permission_required('gestion_usuarios.cliente_user')
def desuscribir(request):
    usuario=request.user
    cliente=Clientes.objects.get(user_id=usuario.id)
    try:
        cliente.suscripcion = False
        cliente.save()
        url_rev=reverse('gestion_usuarios:noticias')+'?subs'
        return redirect(url_rev)
    except:
        url_rev=reverse('gestion_usuarios:noticias')+'?non_subs'
        return redirect(url_rev)

        
