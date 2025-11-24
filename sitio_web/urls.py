from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from usuarios.views import index_view

def root(request):
    return redirect('login')  # o a 'index', según quieras

urlpatterns = [
    path('', root),                  # ruta principal
    path('index/', index_view, name='index'),  # para acceder directamente a index.html
    path('', include('usuarios.urls')),   # rutas de la app usuarios
    path('admin/', admin.site.urls),
]
