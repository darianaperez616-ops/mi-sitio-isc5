from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>✅ SITIO FUNCIONANDO</h1><p>Render deploy fixed</p>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
