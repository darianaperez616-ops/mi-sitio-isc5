from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('acceso_base_datos/', views.acceso_base_datos, name='acceso_base_datos'),
    path('', views.index_view, name='index'),
]
