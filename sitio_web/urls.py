from django.contrib import admin
from django.urls import path, include
from usuarios.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('usuarios/', include('usuarios.urls')),
]
