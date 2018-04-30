from django.contrib.auth.views import login, logout
from django.urls import path
from estudiantes.views import signup

app_name = "estudiantes"

urlpatterns = [
	path('login',login, {'template_name': 'estudiantes/login.html'}, name='login'),
	# logout no tiene template, solo nos saca de la sesion y redirecciona
	path('logout',logout, {'next_page':'/'}, name="logout"),
	path('signup',signup, name="signup"),
]