from django.urls import path
from . import views

urlpatterns=[    
    path('about/',views.about),
    path('hola/',views.hola),
    path('',views.inicio,name='home'),
    path('home/',views.inicio,name='home'),
    path('registros/',views.agregar_registro_actividad,name='registroactividad'),
    path('actividad/',views.agregar_actividad,name='crearactividad'),
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('signout/',views.signout),
    path('calendar/',views.calendar),
    path('daycalendar/',views.calendariodiario),

]