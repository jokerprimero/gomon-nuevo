from django.shortcuts import render

# Create your views here.

def Pag_Principal(request):
    return render(request,'Go_mon/Pag_Principal.html')

def iniciouser(request):
    return render(request,'Go_mon/iniciouser.html')

def inicioadmin(request):
    return render(request,'Go_mon/inicioadmin.html')

def iniciocuid(request):
    return render(request,'Go_mon/iniciocuid.html')

def adm(request):
    return render(request,'Go_mon/adm.html')

def admbanear(request):
    return render(request,'Go_mon/admbanear.html')

def admministrador(request):
    return render(request,'Go_mon/administrador.html')

def Apoderado(request):
    return render(request,'Go_mon/Apoderado.html')

def buscador(request):
    return render(request,'Go_mon/buscador.html')

def calendario(request):
    return render(request,'Go_mon/calendario.html')

def cambio(request):
    return render(request,'Go_mon/cambio.html')

def descripcion(request):
    return render(request,'Go_mon/descripcion.html')

def descripcion2(request):
    return render(request,'Go_mon/descripcion2.html')

<<<<<<< Updated upstream
def Perfil(request):
    return render(request,'Go_mon/Perfil.html')

def perfil_editar(request):
    return render(request,'Go_mon/perfil_editar.html')
=======
def perfil_editar(request):
    return render(request,'Go_mon/perfil_editar.html')

def Perfil(request):
    return render(request,'Go_mon/Perfil.html')
>>>>>>> Stashed changes
