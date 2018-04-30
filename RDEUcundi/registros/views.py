from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from registros.models import Dispositivo, DispositivoRegistro
from estudiantes.models import Estudiante
from registros.forms import RegisterForm
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from django.conf import settings
from django.template import loader
# Create your views here.

class HomeView(TemplateView):
	template_name='registros/home.html'
	#le pasamos en el contexto todos los productos
	def get_context_data(self, *args, **kwargs):
		dispositivos = Dispositivo.objects.all()
		dispo_reg = DispositivoRegistro.objects.all()
		estudiantes = Estudiante.objects.all()
		register_form = RegisterForm()
		return {'dispositivos': dispositivos, 'dispo_reg':dispo_reg, 'estudiantes':estudiantes, 'register_form':register_form}

def crearreg(request):
	form = RegisterForm(request.POST or None)

	if form.is_valid():
		registro = form.save()
		cantidadpedido = registro.cantidad
		disdispo = Dispositivo.objects.get(tipo=registro.dispositivo)
		if registro.devuelto:
			disdispo.cantidad = disdispo.cantidad + cantidadpedido
		# Dismunuyendo el stock
		else:
			disdispo.cantidad = disdispo.cantidad - cantidadpedido
		disdispo.save()
		registro.save()
		dispositivos = Dispositivo.objects.all()
		dispo_reg = DispositivoRegistro.objects.all()
		estudiantes = Estudiante.objects.all()
		register_form = RegisterForm()
		page = loader.get_template('registros/alert.html')
		context = {'respuesta': 'Excelente, Se ha registrado tu solicitud.','dispositivos': dispositivos, 'dispo_reg':dispo_reg, 'estudiantes':estudiantes, 'register_form':register_form}
		return HttpResponse(page.render(context, request))
	return HttpResponseBadRequest()