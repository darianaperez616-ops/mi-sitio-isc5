from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_redirect(request):
    return redirect('login')  # Redirige al login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_redirect),
    path('usuarios/', include('usuarios.urls')),
]
