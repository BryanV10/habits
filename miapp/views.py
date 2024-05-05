from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import RegistroActividad,Actividad
from .forms import RegistroActividadForm,ActividadForm


# Create your views here.
def inicio(request):
    #registrospython=list(RegistroActividad.objects.values())
    registrospython=RegistroActividad.objects.all()
    #actividades=Actividad.objects.all()
    return render(request, "index.html",{
        'registros':registrospython
    })

def crudRegistro(request):
    #RegistroActividad.objects.create()
    return render(request, "crudRegistro.html",{
        'formulario':RegistroActividadForm()
    })

def agregar_registro_actividad(request):
    if request.method == 'POST':
        form = RegistroActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')  # Redirige a donde desees después de agregar el registro
    else:
        form = RegistroActividadForm()
    return render(request, 'crudRegistro.html', {'formulario': form})

def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')  # Redirige a donde desees después de agregar el registro
    else:
        form = ActividadForm()
    return render(request, 'crudActividad.html', {'formulario': form})

def hola(request):
    return render (request, "base.html")

def about(request):
    return HttpResponse("<h1>Sobre...</h1>")