from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio),
    path('about/',views.about),
    path('hola/',views.hola)

]