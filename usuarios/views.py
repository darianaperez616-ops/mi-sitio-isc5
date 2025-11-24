from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    return render(request, 'usuarios/login.html')

def registro_view(request):
    return render(request, 'usuarios/registro.html')

def acceso_base_datos(request):
    return render(request, 'usuarios/base_datos.html')

def index_view(request):
    return render(request, 'usuarios/index.html')

# Vista para procesar el formulario de registro
def procesar_registro(request):
    if request.method == 'POST':
        # Aquí procesarías los datos del formulario
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Lógica de registro...
        return redirect('login')
    return redirect('registro')

# Vista para procesar el formulario de login  
def procesar_login(request):
    if request.method == 'POST':
        # Aquí procesarías los datos del login
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Lógica de autenticación...
        return redirect('acceso_base_datos')
    return redirect('login')
