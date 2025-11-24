from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>¡Mi sitio funciona! 🎉</h1><p>Bienvenido al sitio</p>')

def home(request):
    return render(request, 'usuarios/index.html')
