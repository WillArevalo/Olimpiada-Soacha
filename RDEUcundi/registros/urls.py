from django.urls import path
from registros.views import (
	HomeView, crearreg
)

urlpatterns = [
	path("", HomeView.as_view(),name="home"),
	path("/", crearreg, name="crearreg"),
]