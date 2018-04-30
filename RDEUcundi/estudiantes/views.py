from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy, resolve
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import RedirectView
# Create your views here.
def signup(request):
	#Para post y get
	form = UserCreationForm(request.POST or None)
	#Si el formulario es valido se guarda
	if form.is_valid():
		form.save()
		#logueamos el usuario
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('home')
	#si el formulario no es valido que vuelva a renderizar el mismo formulario
	return render(request,"estudiantes/signup.html", {'form':form})