from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Buscar usuario por email
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
    
    return render(request, 'usuarios/login.html')

def registro_view(request):
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
        
        # Crear usuario en la base de datos
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        user.save()
        
        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión')
        return redirect('login')
    
    return render(request, 'usuarios/registro.html')

def acceso_base_datos(request):
    # Aquí mostrarías información de la base de datos
    users = User.objects.all() if User.objects.exists() else []
    return render(request, 'usuarios/base_datos.html', {'users': users})

def index_view(request):
    return redirect('login')
