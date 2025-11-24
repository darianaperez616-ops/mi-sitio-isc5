from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Usuario, Juego, Puntaje, Configuracion, Actividad
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# -------------------- LOGIN / REGISTRO --------------------
def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'usuarios/registro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ese correo ya está registrado.')
            return render(request, 'usuarios/registro.html')

        User.objects.create_user(username=email, email=email, password=password, first_name=nombre)
        messages.success(request, 'Cuenta creada correctamente.')
        return redirect('login')

    return render(request, 'usuarios/registro.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Correo no registrado.')
            return render(request, 'usuarios/login.html')

        user = authenticate(request, username=user.username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Contraseña incorrecta.')

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# -------------------- VISTAS GENERALES --------------------
def home_view(request):
    return render(request, 'usuarios/home.html')

def index_view(request):
    return render(request, 'usuarios/index.html')


def opciones_view(request):
    return render(request, 'usuarios/opciones.html')

def juegos_view(request):
    return render(request, 'usuarios/juego.html')

def configuracion_view(request):
    return render(request, 'usuarios/configuracion.html')

def creditos_view(request):
    return render(request, 'usuarios/creditos.html')

def encuesta_view(request):
    return render(request, 'usuarios/encuesta.html')

@login_required
def memorama_view(request):
    contexto = {
        'usuario_id': request.user.id
    }
    return render(request, 'usuarios/memorama.html', contexto)


def quiz_view(request):
    return render(request, 'usuarios/quiz.html')

def imagenes_view(request):
    return render(request, 'imagenes.html')

@login_required
def arrastrar_view(request):
    contexto = {
        'usuario_id': request.user.id
    }
    return render(request, 'usuarios/arrastrarysoltar.html', contexto)

def juego2_view(request):
    return render(request, 'usuarios/juego2.html')


# -------------------- ACCESO BASE DE DATOS --------------------
def acceso_base_datos(request):
    error = None
    if request.method == "POST":
        password = request.POST.get("password")
        if password == "D4r14n4BD":
            return redirect("mostrar_base_datos")
        else:
            error = "Contraseña incorrecta"
    return render(request, "usuarios/acceso_base_datos.html", {"error": error})


# -------------------- CRUD COMPLETO --------------------
def mostrar_base_datos(request):
    if request.method == "POST":
        tipo = request.POST.get("tipo_tabla")

        if tipo == "usuario":
            Usuario.objects.create(
                nombre=request.POST.get("nombre"),
                correo=request.POST.get("correo"),
                contrasena=request.POST.get("contrasena")
            )

        elif tipo == "juego":
            Juego.objects.create(
                nombre=request.POST.get("nombre")
            )

        elif tipo == "puntaje":
            usuario = Usuario.objects.get(pk=request.POST.get("usuario"))
            juego = Juego.objects.get(pk=request.POST.get("juego"))
            Puntaje.objects.create(
                usuario=usuario,
                juego=juego,
                puntuacion=request.POST.get("puntuacion"),
                tiempo_segundos=request.POST.get("tiempo")
            )

        elif tipo == "configuracion":
            usuario = Usuario.objects.get(pk=request.POST.get("usuario"))
            Configuracion.objects.create(
                usuario=usuario,
                dificultad=request.POST.get("dificultad"),
                sonido=request.POST.get("sonido") == "on"
            )

        elif tipo == "actividad":
            usuario = Usuario.objects.get(pk=request.POST.get("usuario"))
            Actividad.objects.create(
                usuario=usuario,
                descripcion=request.POST.get("descripcion")
            )

        return redirect("mostrar_base_datos")

    contexto = {
        'usuarios': Usuario.objects.all(),
        'juegos': Juego.objects.all(),
        'puntajes': Puntaje.objects.all(),
        'configuraciones': Configuracion.objects.all(),
        'actividades': Actividad.objects.all()
    }
    return render(request, "usuarios/mostrar_base_datos.html", contexto)


# -------------------- EDITAR --------------------
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        usuario.nombre = request.POST.get("nombre")
        usuario.correo = request.POST.get("correo")
        usuario.contrasena = request.POST.get("contrasena")
        usuario.save()
        messages.success(request, "Usuario actualizado")
        return redirect("mostrar_base_datos")
    return render(request, "usuarios/editar_usuario.html", {"usuario": usuario})

def editar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        juego.nombre = request.POST.get("nombre")
        juego.save()
        messages.success(request, "Juego actualizado")
        return redirect("mostrar_base_datos")
    return render(request, "usuarios/editar_juego.html", {"juego": juego})

def editar_puntaje(request, pk):
    puntaje = get_object_or_404(Puntaje, pk=pk)
    if request.method == "POST":
        puntaje.usuario = get_object_or_404(Usuario, pk=request.POST.get("usuario"))
        puntaje.juego = get_object_or_404(Juego, pk=request.POST.get("juego"))
        puntaje.puntuacion = request.POST.get("puntuacion")
        puntaje.tiempo_segundos = request.POST.get("tiempo")
        puntaje.save()
        messages.success(request, "Puntaje actualizado")
        return redirect("mostrar_base_datos")
    return render(request, "usuarios/editar_puntaje.html", {"puntaje": puntaje, "usuarios": Usuario.objects.all(), "juegos": Juego.objects.all()})

def editar_configuracion(request, pk):
    config = get_object_or_404(Configuracion, pk=pk)
    if request.method == "POST":
        config.usuario = get_object_or_404(Usuario, pk=request.POST.get("usuario"))
        config.dificultad = request.POST.get("dificultad")
        config.sonido = request.POST.get("sonido") == "on"
        config.save()
        messages.success(request, "Configuración actualizada")
        return redirect("mostrar_base_datos")
    return render(request, "usuarios/editar_configuracion.html", {"config": config, "usuarios": Usuario.objects.all()})

def editar_actividad(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == "POST":
        actividad.usuario = get_object_or_404(Usuario, pk=request.POST.get("usuario"))
        actividad.descripcion = request.POST.get("descripcion")
        actividad.save()
        messages.success(request, "Actividad actualizada")
        return redirect("mostrar_base_datos")
    return render(request, "usuarios/editar_actividad.html", {"actividad": actividad, "usuarios": Usuario.objects.all()})


# -------------------- ELIMINAR --------------------
def eliminar_usuario(request, pk):
    get_object_or_404(Usuario, pk=pk).delete()
    messages.success(request, "Usuario eliminado")
    return redirect("mostrar_base_datos")

def eliminar_juego(request, pk):
    get_object_or_404(Juego, pk=pk).delete()
    messages.success(request, "Juego eliminado")
    return redirect("mostrar_base_datos")

def eliminar_puntaje(request, pk):
    get_object_or_404(Puntaje, pk=pk).delete()
    messages.success(request, "Puntaje eliminado")
    return redirect("mostrar_base_datos")

def eliminar_configuracion(request, pk):
    get_object_or_404(Configuracion, pk=pk).delete()
    messages.success(request, "Configuración eliminada")
    return redirect("mostrar_base_datos")

def eliminar_actividad(request, pk):
    get_object_or_404(Actividad, pk=pk).delete()
    messages.success(request, "Actividad eliminada")
    return redirect("mostrar_base_datos")










#---------------------------------------------#




# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Juego, Puntaje, Actividad

@csrf_exempt
def guardar_puntaje(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            juego_nombre = data.get('juego')
            puntaje_valor = data.get('puntaje')
            tiempo = data.get('tiempo')
            usuario_id = data.get('usuario_id')

            usuario = Usuario.objects.get(id=usuario_id)
            juego, created = Juego.objects.get_or_create(nombre=juego_nombre)

            # Guardar puntaje
            Puntaje.objects.create(
                usuario=usuario,
                juego=juego,
                puntuacion=puntaje_valor,
                tiempo_segundos=tiempo
            )

            # Guardar actividad
            Actividad.objects.create(
                usuario=usuario,
                descripcion=f"Jugó {juego_nombre} y obtuvo {puntaje_valor} puntos"
            )

            return JsonResponse({'mensaje': 'Puntaje guardado correctamente'})
        except Exception as e:
            return JsonResponse({'mensaje': f'Error: {str(e)}'}, status=400)
    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)



