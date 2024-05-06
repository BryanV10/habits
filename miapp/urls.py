from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio),
    path('about/',views.about),
    path('hola/',views.hola),
    path('registros/',views.agregar_registro_actividad),
    path('actividad/',views.agregar_actividad),
    path('signup/',views.signup),

]