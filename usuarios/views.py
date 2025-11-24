from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceso_base_datos')
        else:
            messages.error(request, 'Credenciales incorrectas')
    return render(request, 'usuarios/login.html')

def registro_view(request):
    if request.method == 'POST':
        from django.contrib.auth.models import User
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            messages.error(request, 'El usuario ya existe')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('login')
    return render(request, 'usuarios/registro.html')

@login_required
def acceso_base_datos(request):
    return render(request, 'usuarios/acceso_base_datos.html')

@login_required
def panel_base_datos(request):
    # Datos de ejemplo para las tablas
    context = {
        'usuarios': [
            {'id': 1, 'nombre': 'Juan Pérez', 'correo': 'juan@email.com', 'fecha_registro': '2024-01-15'},
            {'id': 2, 'nombre': 'María García', 'correo': 'maria@email.com', 'fecha_registro': '2024-01-14'},
        ],
        'juegos': [
            {'id': 1, 'nombre': 'Adivina el número'},
            {'id': 2, 'nombre': 'Memoria'},
        ]
    }
    return render(request, 'usuarios/panel_base_datos.html', context)

def index_view(request):
    return redirect('login')
