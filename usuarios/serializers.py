from rest_framework import serializers
from .models import Usuario, Juego, Puntaje, Configuracion, Actividad

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__'

class PuntajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntaje
        fields = '__all__'

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'
