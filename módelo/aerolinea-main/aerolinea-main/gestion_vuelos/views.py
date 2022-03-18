from django.forms.forms import Form
from django.utils import timezone
from django.http import Http404
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic.base import TemplateView
from gestion_vuelos.forms import FormVueloNacional, FormVueloInternacional, FormEdit
from gestion_vuelos.models import Vuelos
from django.contrib.auth.decorators import permission_required
from django.urls import reverse


# Create your views here.

@permission_required('gestion_usuarios.admin_user')
def vuelos(request):
    """
    Esta vista permite listar todos los vuelos programados en la base de datos.
    """
    try:
        data=Vuelos.objects.filter(fecha_vuelo__gt=timezone.localtime(timezone.now()).today() ).order_by('fecha_vuelo')
    except:
        raise Http404("No hay vuelos")

    context={
        'data':data
    }
    return render(request, "vuelos.html", context)


@permission_required('gestion_usuarios.admin_user')
def cancelarVuelo(request):

    """
    Recupera la PK y elimina el vuelo de la DB
    """
    
    pk=int(request.POST['pk_hidden'])
    vuelo = Vuelos.objects.get(id=pk)
    vuelo.delete()

    url_rev=reverse('gestion_vuelos:vuelos')+'?True'
    return redirect(url_rev)

@permission_required('gestion_usuarios.admin_user')
def editarVuelo(request, pk):
    
    #Obtiene el vuelo al recuperar la pk.
    vuelo       =   Vuelos.objects.get(id=pk)
    
    #Añade la informacion del vuelo al contexto.
    context={
            'vuelo':vuelo,
        }

    #Recupera el precio y la fecha de vuelo antes de que el usuario ingrese uno.
    oldprice=vuelo.costo
    oldDate=vuelo.fecha_vuelo

    # Se recibe un formulario
    if request.method == 'POST':
        
        # Se obtiene los datos del formulario
        form  =   FormEdit(request.POST, instance=vuelo)

        # Se añade el formulario al contexto.
        context["form"]=form

        # el formulario es valido? Revisar el metodo clean en forms.py
        if form.is_valid():

            # se cargan los datos ingresados, commit=False, impide que se hagn cambios
            # en la base de datos por el momento.
            data=form.save(commit=False)

            # se valida la fecha.
            data.validDate(oldDate)

            # se actualiza la fecha de llegada.
            data.addFechaLLegada()

            # se crea una promocion si aplica.
            data.setPromocion(oldprice)

            # se almacenan los cambios en la base de datos.
            data.save()


            url_rev=reverse('gestion_vuelos:vuelos')+'?True'
            return redirect(url_rev)
        else:
            print(form.errors)
    else:
        form = FormEdit(instance=vuelo)
        context['form']=form

    return render(request,"formulario_editarVuelo.html", context)

@permission_required('gestion_usuarios.admin_user')
def crearVueloNac(request):
    """
    Permite la creacion de vuelos nacionales.
    """

    if request.method=="POST":

        # Se recibe un formulario.
        form=FormVueloNacional(request.POST)

        # El formulario es valido?
        if form.is_valid():

            # se cargan los datos ingresados, commit=False, impide que se hagn cambios
            # en la base de datos por el momento.
            data=form.save(commit=False)

            # se añade un fecha de llegada.
            data.addFechaLLegada()

            # se define el numero de asientos.
            data.asientos()

            # se guarda la informacion en la base de datos.
            data.save()


            url_rev=reverse('gestion_vuelos:vuelos')+'?True'
            return redirect(url_rev)
        else:
            print(form.errors)
    else:
        form=FormVueloNacional()
    return render(request, "formulario_crearVuelo.html", {"form":form})


@permission_required('gestion_usuarios.admin_user')
def crearVueloInt(request):
    """
    Permite la creacion de vuelos internacionales.
    """
    if request.method=='POST': 
        # Se recibe un formulario.
        form=FormVueloInternacional(request.POST)
        # El formulario es valido?
        if form.is_valid():
             # se cargan los datos ingresados, commit=False, impide que se hagn cambios
            # en la base de datos por el momento.
            data=form.save(commit=False)

            # se añade un fecha de llegada.
            data.addFechaLLegada()

            # se define el numero de asientos.
            data.asientos()

            # se guarda la informacion en la base de datos.
            data.save()
            url_rev=reverse('gestion_vuelos:vuelos')+'?True'
            return redirect(url_rev)
        else:
            print(form.errors)
    else:
        form=FormVueloInternacional()
    return render(request, "formulario_crearVuelo.html", {"form":form})


#    #Al acceder a la ruta http://127.0.0.1:8000/gestionVuelos/crearVuelo/ se renderiza el formulario
#    #para presentario en un documento html
#    return render(request, "formulario_crearVuelo.html", {"form":formulario})
#