from django import forms
from .models import RegistroActividad,Actividad,Calendario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class RegistroActividadForm(forms.ModelForm):
    class Meta:
        model = RegistroActividad
        fields = ['actividad', 'calendario', 'hora_inicio', 'duracion_real']

class ActividadForm(forms.ModelForm):
    class Meta:
        model=Actividad
        fields=['nombre','descripcion','prioridad','duracion_estimada']

