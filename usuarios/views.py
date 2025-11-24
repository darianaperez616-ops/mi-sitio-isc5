from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    return render(request, 'usuarios/login.html')

def registro_view(request):
    return render(request, 'usuarios/registro.html')

def acceso_base_datos(request):
    return HttpResponse('<h1 style=\"color: #5b2bc0; text-align: center; margin-top: 100px;\">Base de Datos - FUNCIONANDO</h1><a href=\"/usuarios/login/\" style=\"display: block; text-align: center;\">← Volver al Login</a>')

def index_view(request):
    return redirect('login')
