from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    #registros=list(RegistroActividad.oject.values())
    return render(request, "index.html")

def hola(request):
    return HttpResponse("Hola Mundo")

def about(request):
    return HttpResponse("<h1>Sobre...</h1>")