from django.contrib import admin
from django.urls import path, include, re_path, reverse
from compras_reservas.views import *

app_name='compras_reservas'

urlpatterns = [
    path('reservar/<int:pk>', hacer_reserva, name='reserva'),
    path('ver/reservas/', ver_reservas,name='ver_reservas'),
    path('eliminar/<int:pk>', eliminar_reserva,name='eliminar_reserva'),
    path('modificar/<int:pk>', modificar_reserva ,name='modificar_reserva'),

]