from django.urls import path, include
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('rutas/', views.listar_rutas, name='listar_rutas'),
    path('rutas/crear/', views.crear_ruta, name='crear_ruta'),
]
