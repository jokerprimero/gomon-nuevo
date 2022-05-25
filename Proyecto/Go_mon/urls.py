from django.contrib import admin
from django.urls import path
from .views import Pag_Principal,iniciouser,inicioadmin,iniciocuid,adm,admbanear,admministrador,Apoderado,buscador,calendario,cambio,descripcion,descripcion2,Perfil,perfil_editado

urlpatterns = [
    path('',Pag_Principal,name="Pag_Principal"),
    path('iniciouser/', iniciouser, name="iniciouser"),
    path('inicioadmin/', inicioadmin, name="inicioadmin"),
    path('iniciocuid/', iniciocuid, name="iniciocuid"),
    path('adm/', adm, name="adm"),
    path('admbanear/', admbanear, name="admbanear"),
    path('admministrador/', admministrador, name="admministrador"),
    path('Apoderado/', Apoderado, name ='Apoderado'),
    path('buscador/', buscador, name ='buscador'),
    path('calendario/', calendario, name ='calendario'),
    path('cambio/', cambio, name ='cambio'),
    path('descripcion/', descripcion, name='descripcion'),
    path('descripcion2/', descripcion2, name='descripcion2'),
    path('perfil_editado/', perfil_editado, name='perfil_editado'),
    path('Perfil/', Perfil, name='Perfil'),

    
    
]