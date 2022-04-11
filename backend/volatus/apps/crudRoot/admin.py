from django.contrib import admin

# Register your models here.
from apps.crudRoot.models import Usuario, InfoRoot


admin.site.register(Usuario)
admin.site.register(InfoRoot)

admin.site.site_header = 'Administración de volatus'
admin.site.site_tittle = 'Administración de volatus'
