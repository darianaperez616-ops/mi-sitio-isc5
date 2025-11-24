from usuarios.models import Usuario, Juego, Puntaje, Configuracion, Actividad
import random

# Crear 20 usuarios
for i in range(1, 21):
    Usuario.objects.create(
        correo=f"usuario{i}@example.com",
        contrasena="temporal123"
    )

# Crear 20 juegos
for i in range(1, 21):
    Juego.objects.create(
        nombre=f"Juego{i}",
        descripcion=f"Descripción del Juego{i}",
        dificultad=random.choice(["facil","medio","dificil"])
    )

# Obtener usuarios y juegos para puntajes, configuraciones y actividades
usuarios = list(Usuario.objects.all())
juegos = list(Juego.objects.all())

# Crear 20 puntajes
for i in range(20):
    Puntaje.objects.create(
        usuario=random.choice(usuarios),
        juego=random.choice(juegos),
        puntuacion=random.randint(50,1000),
        tiempo_segundos=random.randint(30,600)
    )

# Crear 20 configuraciones
for i in range(20):
    Configuracion.objects.create(
        usuario=random.choice(usuarios),
        sonido_activado=random.choice([True, False]),
        musica_activada=random.choice([True, False]),
        dificultad_preferida=random.choice(["facil","medio","dificil"]),
        tema_oscuro=random.choice([True, False]),
        notificaciones=random.choice([True, False])
    )

# Crear 20 actividades
for i in range(20):
    Actividad.objects.create(
        usuario=random.choice(usuarios),
        tipo_actividad=random.choice(["login","logout","juego","config"]),
        descripcion=f"Actividad {i+1}",
        ip_address=f"192.168.1.{i+1}"
    )

print("20 registros creados en todas las tablas")
