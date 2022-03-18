from django.contrib import admin
from django.urls import path, include, re_path, reverse
from busqueda_noticias.views import *

app_name='busqueda_noticias'

urlpatterns = [
    path('buscar', buscar_vuelo, name='buscar'),
    path('ver/<int:pk>/',ver_vuelo,name="ver"),    
]