from django.db import models

# Create your models here.
class Estudiante(models.Model):
	codigo = models.CharField(max_length=255, unique=True)
	nombre = models.CharField(max_length=255)
	telefono = models.CharField(max_length=255)
	carrera = models.CharField(max_length=255)
	def __str__(self):
		return self.nombre