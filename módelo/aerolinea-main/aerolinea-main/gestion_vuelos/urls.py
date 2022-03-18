from django.contrib import admin
from django.urls import path, include
from gestion_vuelos.views import *

app_name='gestion_vuelos'
urlpatterns = [
    path('vuelos/',vuelos,name="vuelos"),
    path('crearVueloNac/',crearVueloNac,name='crearVueloNac'),
    path('crearVueloInt/',crearVueloInt,name='crearVueloInt'),
    path('editarVuelo/<int:pk>/',editarVuelo,name="editarVuelo"),
    path('cancelarVuelo/',cancelarVuelo,name="cancelarVuelo"),
]