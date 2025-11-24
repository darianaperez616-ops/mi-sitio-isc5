from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'usuarios/login.html')

def registro_view(request):
    return render(request, 'usuarios/registro.html')

def acceso_base_datos(request):
    return render(request, 'usuarios/acceso_base_datos.html')

def home_view(request):
    return render(request, 'usuarios/home.html')

def index_view(request):
    return render(request, 'usuarios/index.html')

# Agrega aquí cualquier otra vista que necesites
def opciones_view(request):
    return render(request, 'usuarios/opciones.html')

def configuracion_view(request):
    return render(request, 'usuarios/configuracion.html')

def creditos_view(request):
    return render(request, 'usuarios/creditos.html')
