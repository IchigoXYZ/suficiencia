from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Direccion)
admin.site.register(Trabajador)
admin.site.register(TrabajadorNoDocente)
admin.site.register(TrabajadorDocente)