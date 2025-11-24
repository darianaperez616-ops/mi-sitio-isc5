from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return HttpResponse('''
    <h1>🔐 LOGIN - SITIO FUNCIONANDO</h1>
    <form>
        <input type=\"text\" placeholder=\"Usuario\"><br>
        <input type=\"password\" placeholder=\"Contraseña\"><br>
        <button>Entrar</button>
    </form>
    <p><a href=\"/admin/\">Administración</a></p>
    <p style=\"color: green;\">✅ El sitio está funcionando en la nube</p>
    ''')

def index_view(request):
    return HttpResponse('<h1>¡Página principal!</h1>')

def home(request):
    return render(request, 'usuarios/index.html')
