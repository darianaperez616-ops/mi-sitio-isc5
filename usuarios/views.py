from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'usuarios/login.html')

def registro_view(request):
    return HttpResponse('<h1>Página de registro</h1><p>Próximamente...</p>')

def index_view(request):
    return HttpResponse('INDEX')
