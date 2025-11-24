from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>✅ SITIO REPARADO</h1><p>Despliegue exitoso</p>')

urlpatterns = [path('', home)]
