from django import forms
from .models import RegistroActividad,Actividad,Calendario

class RegistroActividadForm(forms.ModelForm):
    class Meta:
        model = RegistroActividad
        fields = ['actividad', 'calendario', 'hora_inicio', 'duracion_real']

class ActividadForm(forms.ModelForm):
    class Meta:
        model=Actividad
        fields=['nombre','descripcion','prioridad','duracion_estimada']

