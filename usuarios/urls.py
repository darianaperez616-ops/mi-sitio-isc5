from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('acceso_base_datos/', views.acceso_base_datos, name='acceso_base_datos'),
    path('procesar_registro/', views.procesar_registro, name='procesar_registro'),
    path('procesar_login/', views.procesar_login, name='procesar_login'),
]
