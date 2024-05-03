from django.shortcuts import render
from django.http import HttpResponse
from .models import Actividad,RegistroActividad

# Create your views here.
def inicio(request):
    #registrospython=list(RegistroActividad.objects.values())
    registrospython=RegistroActividad.objects.all()
    #actividades=Actividad.objects.all()
    return render(request, "index.html",{
        'registros':registrospython
    })

def hola(request):
    return HttpResponse("Hola Mundo")

def about(request):
    return HttpResponse("<h1>Sobre...</h1>")