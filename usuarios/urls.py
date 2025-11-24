from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index_view, name='index'),
    path('opciones/', views.opciones_view, name='opciones'),
    path('imagenes/', views.imagenes_view, name='imagenes'),
    path('juegos/', views.juegos_view, name='juegos'),
    path('configuracion/', views.configuracion_view, name='configuracion'),
    path('creditos/', views.creditos_view, name='creditos'),
    path('encuesta/', views.encuesta_view, name='encuesta'),
    path('memorama/', views.memorama_view, name='memorama'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('arrastrar/', views.arrastrar_view, name='arrastrar'),
    path('juego2/', views.juego2_view, name='juego2'),

    # BASE DE DATOS
    path('acceso_base_datos/', views.acceso_base_datos, name='acceso_base_datos'),
    path('mostrar_base_datos/', views.mostrar_base_datos, name='mostrar_base_datos'),

    # CRUD
    path('editar_usuario/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('editar_juego/<int:pk>/', views.editar_juego, name='editar_juego'),
    path('eliminar_juego/<int:pk>/', views.eliminar_juego, name='eliminar_juego'),
    path('editar_puntaje/<int:pk>/', views.editar_puntaje, name='editar_puntaje'),
    path('eliminar_puntaje/<int:pk>/', views.eliminar_puntaje, name='eliminar_puntaje'),
    path('editar_configuracion/<int:pk>/', views.editar_configuracion, name='editar_configuracion'),
    path('eliminar_configuracion/<int:pk>/', views.eliminar_configuracion, name='eliminar_configuracion'),
    path('editar_actividad/<int:pk>/', views.editar_actividad, name='editar_actividad'),
    path('eliminar_actividad/<int:pk>/', views.eliminar_actividad, name='eliminar_actividad'),




    
    path('guardar_puntaje/', views.guardar_puntaje, name='guardar_puntaje'),


]
