from django.contrib import admin
from django.urls import path
from .views import Pag_Principal,iniciouser,adm,admbanear,admministrador,Apoderado,buscador,calendario,cambio,descripcion,descripcion2

urlpatterns = [
    path('',Pag_Principal,name="Pag_Principal"),
    path('iniciouser/', iniciouser, name="iniciouser"),
    path('adm/', adm, name="adm"),
    path('admbanear/', admbanear, name="admbanear"),
    path('admministrador/', admministrador, name="admministrador"),
    path('Apoderado/', Apoderado, name ='Apoderado'),
    path('buscador/', buscador, name ='buscador'),
    path('calendario/', calendario, name ='calendario'),
    path('cambio/', cambio, name ='cambio'),
    path('descripcion/', descripcion, name='descripcion'),
    path('descripcion2/', descripcion2, name='descripcion2'),
    
    
]