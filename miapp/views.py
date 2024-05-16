from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from .models import RegistroActividad,Actividad
from .forms import RegistroActividadForm,ActividadForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
import json

# Create your views here.
def inicio(request):
    #registrospython=list(RegistroActividad.objects.values())
    registrospython=RegistroActividad.objects.all().order_by('calendario')
    #actividades=Actividad.objects.all()
    return render(request, "index.html",{
        'registros':registrospython
    })

def calendar(request):
    
    registrospython=RegistroActividad.objects.all().order_by('calendario')    
    """return render(request, "calendario.html",{
        'registros':registrospython    })"""
    
    #eventos = [{'title': acto.actividad, 'start': acto.calendario.strftime('%Y-%m-%d'), 'end': acto.calendario.strftime('%Y-%m-%d')} for acto in registrospython]
    #eventos_json = json.dumps(eventos)

    """eventos = []
    for acto in registrospython:
        evento = {
            'title': acto.actividad,
            'start': acto.calendario.strftime('%Y-%m-%d'),
            'end': acto.calendario.strftime('%Y-%m-%d')
        }
        eventos.append(evento)
    eventos_json = json.dumps(eventos)

    """
    eventos_json = []
    for evento in registrospython:
        eventos_json.append({
            #'title': evento.actividad,
            'title': evento.actividad.nombre,
            'start': evento.calendario.isoformat(),
            'end': evento.calendario.isoformat()
        })
        eventos_jso=json.dumps(eventos_json)
    eventos=str(eventos_jso).strip('[]')
    print(eventos_json)
    print(eventos_jso)
    print('holabola')
    #for e in eventos_json:
    print(eventos_json[2]['title'])
    print(eventos_json[2]['start'])
    print(eventos_json[2]['end'])

    #eventos_json = list(RegistroActividad.objects.all().values())
    #eventos_json_str = json.dumps(eventos_json)  
    
    return render(request, 'calendario.html', {'eventos_json': eventos_jso,'registros':registrospython})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')  # Redirige a la página de inicio después del registro exitoso
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'formulario': form})
    
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'formulario': form})

def signout(request):
    logout(request)
    return redirect('/home')

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
            return redirect('/home')  # Redirige a donde desees después de agregar el registro
    else:
        form = RegistroActividadForm()
    return render(request, 'crudRegistro.html', {'formulario': form})

def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')  # Redirige a donde desees después de agregar el registro
    else:
        form = ActividadForm()
    return render(request, 'crudActividad.html', {'formulario': form})

    
def hola(request):
    return render (request, "base.html")

def about(request):
    return HttpResponse("<h1>Sobre...</h1>")