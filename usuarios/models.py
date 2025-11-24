from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Puntaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    tiempo_segundos = models.IntegerField()

    def __str__(self):
        return f"{self.usuario} - {self.juego}: {self.puntuacion}"


class Configuracion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dificultad = models.CharField(max_length=20, default="Normal")
    sonido = models.BooleanField(default=True)


class Actividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
