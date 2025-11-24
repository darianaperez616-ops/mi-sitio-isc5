
from django.contrib import admin
from .models import Usuario, Juego, Puntaje, Configuracion, Actividad

# Registramos cada modelo para que aparezca en el admin
admin.site.register(Usuario)
admin.site.register(Juego)
admin.site.register(Puntaje)
admin.site.register(Configuracion)
admin.site.register(Actividad)
