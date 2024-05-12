from django import forms
from .models import RegistroActividad,Actividad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

from django import forms

class MiFormulario(forms.Form):
    campo_texto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    campo_correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # Otros campos y widgets...


class RegistroActividadForm(forms.ModelForm):
    class Meta:
        model = RegistroActividad
        fields = ['actividad', 'calendario', 'hora_inicio', 'duracion_real']
        widgets = {
            'actividad': forms.Select(attrs={'class': 'form-control'}),
            'calendario': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hora_inicio'].widget = forms.TimeInput(attrs={'type': 'time','class': 'form-control'})
        self.fields['duracion_real'].widget = forms.TimeInput(attrs={'type': 'time','class': 'form-control'})
        

class ActividadForm(forms.ModelForm):
    class Meta:
        model=Actividad
        fields=['nombre','descripcion','prioridad','duracion_estimada']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'duracion_estimada': forms.TimeInput(attrs={'type': 'time','class': 'form-control'}),
            
        }      

