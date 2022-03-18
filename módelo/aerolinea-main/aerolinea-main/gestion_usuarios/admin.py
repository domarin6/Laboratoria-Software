from django.contrib import admin
from gestion_usuarios.models import *
# Register your models here.

class CamposAdmin(admin.ModelAdmin):
    field=['user', 'DNI']


admin.site.register(Administradores, CamposAdmin)
admin.site.site_header="Administracion MarmotaFly"
admin.site.site_Title="Administracion MarmotaFly"
