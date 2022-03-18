"""aerolinea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestion_usuarios.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('perfil/', include('gestion_usuarios.urls', namespace='gestion_usuarios') ),
    path('gestionVuelos/', include('gestion_vuelos.urls', namespace='gestion_vuelos')),
    path('buscar/', include('busqueda_noticias.urls', namespace='busqueda_noticias')),
    path('vuelos/', include('compras_reservas.urls', namespace='compras_reservas')),
    path('finanzas/', include('modulo_financiero.urls', namespace='modulo_financiero')),
]
