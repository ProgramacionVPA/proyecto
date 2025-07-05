from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Puedes agregar campos extra aquí si lo necesitas
    pass

class Ruta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    hora_salida = models.TimeField()
    dias = models.CharField(max_length=100)
    cupos_disponibles = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.usuario.username})"