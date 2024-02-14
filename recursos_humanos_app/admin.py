from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Direccion)

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ["carnet_identidad", "nombre"]
    search_fields = ["carnet_identidad", "nombre"]

admin.site.register(TrabajadorNoDocente)
admin.site.register(TrabajadorDocente)