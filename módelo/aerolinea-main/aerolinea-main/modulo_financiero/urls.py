from django.contrib import admin
from django.urls import path, include
from modulo_financiero.views import *

app_name='modulo_financiero'
urlpatterns = [
    path('tarjetas/',tarjetas,name="tarjetas"),
    path('add_debit/',agregar_tarjeta_debito,name='add_debit'),
    path('add_credit/',agregar_tarjeta_credito,name='add_credit'),
    path('add_saldo/',add_saldo,name='add_saldo'),
    path('add_cupo/',add_cupo,name='add_cupo'),
    path('edit_debit/<int:pk>',editar_tarjeta_debito,name='edit_debit'),
    path('edit_credit/<int:pk>',editar_tarjeta_credito,name='edit_credit'),
    path('delete_debit/',cancelar_tarjeta_debito,name='delete_debit'),
    path('delete_credit/',cancelar_tarjeta_credito,name='delete_credit'),
    #path('delete/',crearVueloInt,name='delete'),
    #path('update/<int:pk>/',editarVuelo,name="update"),
    #path('/',cancelarVuelo,name="cancelarVuelo"),
]