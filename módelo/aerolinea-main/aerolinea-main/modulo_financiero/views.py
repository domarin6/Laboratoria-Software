from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from gestion_usuarios.models import Clientes
from django.urls import reverse
from django.contrib.auth.decorators import permission_required

from modulo_financiero.models import TarjetaCredito, TarjetaDebito
from modulo_financiero.forms import TarjetaDebitoForm, TarjetaCreditoForm, EditDebitForm
# Create your views here.
@permission_required('gestion_usuarios.cliente_user')
def tarjetas(request):
    cliente = Clientes.objects.get(user_id=request.user.id)
    try:
        debit_cards=TarjetaDebito.objects.filter(cliente_id = cliente.id).values('id','numero','saldo')
        credit_cards=TarjetaCredito.objects.filter(cliente_id = cliente.id).values('id','numero','cupo')
    except:
        print("error")

    context  = {
        'debit_cards':debit_cards,
        'credit_cards':credit_cards,
        'tam_debit':len(debit_cards),
        'tam_credit':len(credit_cards),
    }
    return render(request, "tarjetas.html", context)

@permission_required('gestion_usuarios.cliente_user')
def agregar_tarjeta_debito(request):
    usuario=request.user
    if request.method == 'POST':
        form    = TarjetaDebitoForm(request.POST)
        if form.is_valid():
            data            = form.save(commit=False)
            data.cliente    = Clientes.objects.get(user_id=usuario.id)
            data.save()

            url_rev         = reverse('modulo_financiero:tarjetas')+'?True'
            return redirect(url_rev)
        else:
            print(form.errors)
    else:
        form    = TarjetaDebitoForm()
    return render(request, "agregar_tarjeta_debito.html", {'form':form})

@permission_required('gestion_usuarios.cliente_user')
def agregar_tarjeta_credito(request):
    usuario=request.user
    if request.method == 'POST':
        form    = TarjetaCreditoForm(request.POST)
        if form.is_valid():
            data            = form.save(commit=False)
            data.cliente    = Clientes.objects.get(user_id=usuario.id)
            data.save()

            url_rev         = reverse('modulo_financiero:tarjetas')+'?True'
            return redirect(url_rev)
        else:
            print(form.errors)
    else:
        form    = TarjetaCreditoForm()
    return render(request, "agregar_tarjeta_credito.html", {'form':form})


@permission_required('gestion_usuarios.cliente_user')
def add_saldo(request):
    """
    Recuperamos la Pk
    """
    pk          =int(request.POST['pk_hidden'])
    new_saldo   =int(request.POST['saldo'])
    tarjeta     =TarjetaDebito.objects.get(id=pk)
    if tarjeta.add_saldo(new_saldo):
        tarjeta.save()
        url_rev=reverse('modulo_financiero:tarjetas')+'?saldo'
        return redirect(url_rev)
    else:
        url_rev=reverse('modulo_financiero:tarjetas')+'?non_saldo'
        return redirect(url_rev)

@permission_required('gestion_usuarios.cliente_user')
def editar_tarjeta_debito(request, pk):
    """
    Recuperamos la Pk
    """
    tarjeta     =TarjetaDebito.objects.get(id=pk)
    if request.method == 'POST':
        form = TarjetaDebitoForm(request.POST, instance=tarjeta)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            url_rev=reverse('modulo_financiero:tarjetas')+'?True'
            return redirect(url_rev)
        else:
            print(form.errors)
    else:
        form = TarjetaDebitoForm(instance=tarjeta)
        print(form)

    return render(request, "editar_tarjeta_debito.html", {'form':form, 'tarjeta':tarjeta})


@permission_required('gestion_usuarios.cliente_user')
def editar_tarjeta_credito(request, pk):
    """
    Recuperamos la Pk
    """
    tarjeta     =TarjetaCredito.objects.get(id=pk)
    if request.method == 'POST':
        form = TarjetaCreditoForm(request.POST, instance=tarjeta)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            url_rev=reverse('modulo_financiero:tarjetas')+'?True'
            return redirect(url_rev)
        else:
            print(form.errors)
    else:
        form = TarjetaCreditoForm(instance=tarjeta)
        print(form)

    return render(request, "editar_tarjeta_credito.html", {'form':form, 'tarjeta':tarjeta})


@permission_required('gestion_usuarios.cliente_user')
def add_cupo(request):
    """
    Recuperamos la Pk
    """
    pk          =int(request.POST['pk_hidden'])
    new_saldo   =int(request.POST['cupo'])
    tarjeta     =TarjetaCredito.objects.get(id=pk)
    if tarjeta.add_cupo(new_saldo):
        tarjeta.save()
        url_rev=reverse('modulo_financiero:tarjetas')+'?saldo'
        return redirect(url_rev)
    else:
        url_rev=reverse('modulo_financiero:tarjetas')+'?non_saldo'
        return redirect(url_rev)


@permission_required('gestion_usuarios.cliente_user')
def cancelar_tarjeta_debito(request):
    """
    Recuperamos la PK
    """
    pk          =int(request.POST['pk_hidden'])
    tarjeta     =TarjetaDebito.objects.get(id=pk)

    try:
        tarjeta.delete()
        url_rev=reverse('modulo_financiero:tarjetas')+'?delete'
    except:
        url_rev=reverse('modulo_financiero:tarjetas')+'?non_delete'
    return redirect(url_rev)


@permission_required('gestion_usuarios.cliente_user')
def cancelar_tarjeta_credito(request):
    """
    Recuperamos la PK
    """
    pk          =int(request.POST['pk_hidden'])
    tarjeta     =TarjetaCredito.objects.get(id=pk)

    try:
        tarjeta.delete()
        url_rev=reverse('modulo_financiero:tarjetas')+'?delete'
    except:
        url_rev=reverse('modulo_financiero:tarjetas')+'?non_delete'

    return redirect(url_rev)