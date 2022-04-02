from django.contrib import admin

# Register your models here.
from .models import Administradores, InfoRoot

admin.site.register(Administradores)
admin.site.register(InfoRoot)
