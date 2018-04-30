from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

class Dispositivo(models.Model):
	serial = models.CharField(max_length=255, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	tipo = models.CharField(max_length=255)
	cantidad = models.IntegerField()
	estado = models.TextField()

	def __str__(self):
		return self.tipo

class DispositivoRegistro(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	dispositivo = models.ForeignKey(
		'registros.Dispositivo',
		on_delete = models.CASCADE,
	)
	estudiante = models.ForeignKey(
		'estudiantes.Estudiante',
		on_delete=models.CASCADE,
	)
	cantidad = models.PositiveSmallIntegerField()
	estado = models.TextField()
	devuelto = models.BooleanField()
	def __str__(self):
		return 'El equipo {} ha sido solicitado'.format(self.dispositivo)
