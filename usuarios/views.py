from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'usuarios/login.html')

def registro_view(request):
    return render(request, 'usuarios/registro.html')

def acceso_base_datos(request):
    return HttpResponse('<h1>Base de Datos</h1><a href=\"/\">← Volver</a>')

def index_view(request):
    return HttpResponse('INDEX')
