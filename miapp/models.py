from django.db import models
from django.utils import timezone

# Create your models here.

class Actividad(models.Model):
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)
    duracion_estimada = models.DurationField()

    def __str__(self):
        return self.nombre
    

class RegistroActividad(models.Model):
    actividad = models.ForeignKey('Actividad', on_delete=models.CASCADE)    
    calendario=models.DateField()
    hora_inicio = models.TimeField(default=timezone.now)
    duracion_real = models.DurationField()

    def __str__(self):
        return f"{self.actividad.nombre} - {self.calendario} - {self.hora_inicio}"
