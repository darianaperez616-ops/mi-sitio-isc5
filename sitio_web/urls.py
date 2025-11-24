from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def emergency_page(request):
    html = '''
    <html>
    <body style='background: black; color: white; padding: 50px; font-family: Arial;'>
        <h1>🎯 SITIO FUNCIONANDO - ERROR EN LOGIN</h1>
        <p><strong>✅ El servidor está activo</strong></p>
        <p>❌ Hay un error en la vista login</p>
        <hr>
        <h3>Prueba estas URLs:</h3>
        <a href='/admin/' style='color: yellow;'>🔧 PANEL ADMIN</a><br>
        <a href='/usuarios/login/' style='color: yellow;'>🚪 LOGIN DIRECTO</a><br>
        <a href='/usuarios/index/' style='color: yellow;'>🏠 PÁGINA PRINCIPAL</a>
    </body>
    </html>
    '''
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', emergency_page),  # Página principal temporal
    path('usuarios/', include('usuarios.urls')),
]
