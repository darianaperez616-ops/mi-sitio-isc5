from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def login_view(request):
    # Vista SIMPLE sin base de datos por ahora
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        messages.success(request, f'Login exitoso para {email}')
        return redirect('acceso_base_datos')
    
    return render(request, 'usuarios/login.html')

def registro_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        messages.success(request, f'Usuario {email} registrado exitosamente')
        return redirect('login')
    
    return render(request, 'usuarios/registro.html')

def acceso_base_datos(request):
    return HttpResponse('''
    <html>
    <head>
        <style>
            body { 
                font-family: Arial; 
                background: linear-gradient(135deg, #b589f6, #5e2ebd);
                color: white;
                padding: 40px;
            }
            a { color: white; }
        </style>
    </head>
    <body>
        <h1>Base de Datos</h1>
        <p>Página de base de datos funcionando</p>
        <a href="/usuarios/login/">← Volver al Login</a>
    </body>
    </html>
    ''')

def index_view(request):
    return redirect('login')
