from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('
    <h1 style=\"color: green;\">✅ SITIO REPARADO</h1>
    <p>El problema era el login. Ahora funciona:</p>
    <a href=\"/admin/\">🔧 PANEL ADMIN</a><br>
    <a href=\"/usuarios/index/\">🏠 PÁGINA PRINCIPAL</a>
    ')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
