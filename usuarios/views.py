from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    # Prueba simple - sin lógica compleja
    return render(request, 'usuarios/login.html')

# ... (mantén las otras vistas)
