from django.shortcuts import render
from django.http import HttpResponse

# Vistas principales
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

def opciones_view(request):
    return render(request, 'usuarios/opciones.html')

def configuracion_view(request):
    return render(request, 'usuarios/configuracion.html')

def creditos_view(request):
    return render(request, 'usuarios/creditos.html')

def encuesta_view(request):
    return render(request, 'usuarios/encuesta.html')

# Vistas de juegos
def memorama_view(request):
    return render(request, 'usuarios/memorama.html')

def quiz_view(request):
    return render(request, 'usuarios/quiz.html')

def arrastrar_view(request):
    return render(request, 'usuarios/arrastrarysoltar.html')

def juego2_view(request):
    return render(request, 'usuarios/juego2.html')

def imagenes_view(request):
    return render(request, 'usuarios/juego.html')

def juegos_view(request):
    return render(request, 'usuarios/juego.html')

# Vistas de base de datos (simplificadas por ahora)
def mostrar_base_datos(request):
    return HttpResponse('<h1>Base de Datos</h1><p>Función en desarrollo</p>')

def editar_usuario(request, pk):
    return HttpResponse(f'<h1>Editar Usuario {pk}</h1>')

def editar_juego(request, pk):
    return HttpResponse(f'<h1>Editar Juego {pk}</h1>')

def editar_puntaje(request, pk):
    return HttpResponse(f'<h1>Editar Puntaje {pk}</h1>')

def editar_configuracion(request, pk):
    return HttpResponse(f'<h1>Editar Configuración {pk}</h1>')

def editar_actividad(request, pk):
    return HttpResponse(f'<h1>Editar Actividad {pk}</h1>')
