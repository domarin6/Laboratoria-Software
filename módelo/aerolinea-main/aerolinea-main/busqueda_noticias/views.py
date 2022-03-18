from typing import List
from django.utils import timezone
from django.shortcuts import redirect, render
from busqueda_noticias import capital
from django.urls import reverse
from django.contrib.auth.decorators import permission_required

from busqueda_noticias.capital import Capital

#list
from django.core.paginator import Paginator

from busqueda_noticias.forms import *
from gestion_usuarios.models import Clientes
from gestion_vuelos.models import *
# Create your views here.

ZONA = {'Madrid': 'Europe/Madrid',
            'Londres': 'Europe/London',
            'New York': 'America/New_York',
            'Buenos Aires':'America/Argentina/Buenos_Aires',
    }

def buscar_vuelo(request):
    usuario = request.user
    vuelo_imagen=list()
    capital         = Capital()
    if request.method=='POST':
        lista=[]
        form=FormBusqueda(request.POST)
        
        if form.is_valid():
            f=form.cleaned_data
            for i,j in f.items():
                if j is None or j=='':
                    lista.append(i)
            for l in lista:
                del f[l]
            vuelos=Vuelos.objects.filter(**f)
            #vuelos=Vuelos.objects.filter(tipo_vuelo='nacional')
            for vuelo in vuelos:
              imagen      =   capital.url_capital(vuelo.destino)
              vuelo_imagen.append([vuelo,imagen])
            if usuario.is_authenticated:
                cliente=Clientes.objects.get(user_id=usuario.id)
                return render(request,'Resultado_busqueda.html',{'vuelos':vuelo_imagen,'zona':ZONA, 'suscripcion':cliente.suscripcion})
            else:
                return render(request,'resultado.html',{'vuelos':vuelo_imagen,'zona':ZONA, 'suscripcion':False}) 
            #try: 
             #   cliente = Clientes.objects.get(user_id=usuario.id)
              #  return render(request,'Resultado_busqueda.html',{'vuelos':vuelo_imagen})
           # except:
            #    return render(request,'resultado.html',{'vuelos':vuelo_imagen}) 
        else:
            return redirect('busqueda_noticias:buscar')
    elif request.method=='GET':
        form=FormBusqueda()
        try: 
            cliente = Clientes.objects.get(user_id=usuario.id)
            return render(request,'busqueda_prueba.html', {'form':form})
        except:
            return render(request,'busqueda.html', {'form':form})
            
        


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

    return render(request, 'noticias.html', {'page_obj': page_obj, 'zona':ZONA, 'suscripcion':cliente.suscripcion})

def ver_vuelo (request, pk):
    capital =   Capital()
    vuelo   =   Vuelos.objects.get(id=pk)

    zona    =   None
    if vuelo.tipo_vuelo == "internacional":
        zona    = ZONA.get(vuelo.destino)

    imagen =  capital.url_capital(vuelo.destino) 

    return render(request, 'vuelo.html', {'vuelo': vuelo, 'zona':zona, 'imagen': imagen})

@permission_required('gestion_usuarios.cliente_user')
def suscribir(request):
    usuario=request.user
    cliente=Clientes.objects.get(user_id=usuario.id)
    try:
        cliente.suscripcion = True
        cliente.save()
        url_rev=reverse('busqueda_noticias:noticias')+'?subs'
        return redirect(url_rev)
    except:
        url_rev=reverse('busqueda_noticias:noticias')+'?non_subs'
        return redirect(url_rev)


@permission_required('gestion_usuarios.cliente_user')
def desuscribir(request):
    usuario=request.user
    cliente=Clientes.objects.get(user_id=usuario.id)
    try:
        cliente.suscripcion = False
        cliente.save()
        url_rev=reverse('busqueda_noticias:noticias')+'?subs'
        return redirect(url_rev)
    except:
        url_rev=reverse('busqueda_noticias:noticias')+'?non_subs'
        return redirect(url_rev)

