from django.contrib import admin
from .models import RegistroActividad,Calendario,Actividad
# Register your models here.

admin.site.register(Actividad)
admin.site.register(Calendario)
admin.site.register(RegistroActividad)
