from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from compras_reservas.forms import ReservaForm
from compras_reservas.models import Reservas, Viajero
from gestion_vuelos.models import Vuelos
from gestion_usuarios.models import Clientes

from django.contrib.auth.decorators import permission_required



from datetime import datetime

@permission_required('gestion_usuarios.cliente_user')
def hacer_reserva(request, pk):
    if request.method=='POST':
        accion=request.POST['accion']
        form=ReservaForm(request.POST)
        if form.is_valid():

            pasajero=form.save(commit=False)

            if pasajero.menor_edad():
                adulto=Viajero.objects.filter(DNI=pasajero.acompañante).first()
                if adulto is None:
                    url_rev=reverse('compras_reservas:reserva',kwargs={'pk':pk} )+'?False'
                    return redirect(url_rev)

            vuelo_=Vuelos.objects.get(id=pk)
            usuario=Clientes.objects.get(DNI=request.user.clientes.DNI)
            reserva=Reservas(cliente=usuario,viajero=pasajero,vuelo=vuelo_,estado_reserva=1,creacion_reserva=datetime.now())
            pasajero.save()
            reserva.save()

            if accion=='guardar':
                return redirect('compras_reservas:ver_reservas')
            elif accion=='reserva':
                return redirect(reverse('compras_reservas:reserva',kwargs={'pk':pk}))

    elif request.method=='GET':
        form=ReservaForm()

    return render(request,'compras_reservas/Registro_reservas.html',{'form':form,'pk':pk})

@permission_required('gestion_usuarios.cliente_user')
def ver_reservas(request):
    reservas=Reservas.objects.filter(cliente_id=request.user.clientes.id)
    return render(request,'compras_reservas/Reservas.html',{'reservas':reservas})

@permission_required('gestion_usuarios.cliente_user')
def eliminar_reserva(request,pk):
    reserva=Reservas.objects.get(id=pk)
    viajero=Viajero.objects.get(id=reserva.viajero_id)
    viajeros_m=Viajero.objects.filter(acompañante=viajero.DNI)
    if viajero.acompañante is None:
        for v in viajeros_m:
            v.delete()

    reserva.delete()
    viajero.delete()

    return redirect('compras_reservas:ver_reservas')

@permission_required('gestion_usuarios.cliente_user')
def modificar_reserva(request,pk):
    if request.method=='POST':
        viajero=Viajero.objects.get(id=pk)
        form=ReservaForm(request.POST,instance=viajero)
        if form.is_valid():
            form.save()
            return redirect('compras_reservas:ver_reservas')
    elif request.method=='GET':
        viajero=Viajero.objects.get(id=pk)
        form=ReservaForm(instance=viajero)
    return render(request,'compras_reservas/Modificar_reserva.html',{'form':form, 'pk':pk})




