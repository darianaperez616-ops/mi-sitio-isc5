from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {user.email}!')
                return redirect('acceso_base_datos')
            else:
                messages.error(request, 'Correo o contraseña incorrectos')
        except User.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos')
    
    return render(request, 'usuarios/login.html')

def registro_view(request):
    return render(request, 'usuarios/registro.html')

# ESTA ES LA FUNCIÓN QUE FALTABA
def procesar_registro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registro')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado')
            return redirect('registro')
        
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error en el registro: {str(e)}')
    
    return redirect('registro')

def procesar_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('acceso_base_datos')
            else:
                messages.error(request, 'Correo o contraseña incorrectos')
                return redirect('login')
                
        except User.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos')
            return redirect('login')
    
    return redirect('login')

def acceso_base_datos(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Debes iniciar sesión para ver esta página')
        return redirect('login')
    
    users = User.objects.all()
    return render(request, 'usuarios/base_datos.html', {'users': users})

def index_view(request):
    return redirect('login')

# Funciones de diagnóstico (opcionales)
def diagnostic_view(request):
    return HttpResponse('<h1>✅ Django está funcionando</h1>')

def diagnostic_template(request):
    return render(request, 'usuarios/diagnostic.html')
