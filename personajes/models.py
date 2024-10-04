from django.db import models
from django.utils import timezone  # Para obtener la fecha actual
from django.conf import settings

#Como crear un modelo animal

class Personaje (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    historia = models.CharField(max_length=100)
    raza = models.TextField(max_length=30)

    def __str__(self):
        return self.nombre

class Hechicero(models.Model):
    user = models.CharField(max_length=100)
    magia = models.TextField(max_length=100)
    fechacreacion = models.DateTimeField(default=timezone.now)
    
class Dexteridad(models.Model):
    nombre = models.CharField(max_length=100)
    destreza = models.CharField(max_length=100)
    fechacreacion = models.DateTimeField(default=timezone.now)
    
    
class Piromano(models.Model):
    nombre = models.CharField(max_length=100)
    temperaturafuego = models.CharField(max_length=100)
    fechacreacion = models.DateTimeField(default=timezone.now)


class Marginado(models.Model):
    nombre = models.CharField(max_length=100)
    resistencia = models.CharField(max_length=100)
    fechacreacion = models.DateTimeField(default=timezone.now)

