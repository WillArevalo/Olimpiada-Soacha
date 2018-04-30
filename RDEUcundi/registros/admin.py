from django.contrib import admin
from registros.models import (
	Dispositivo,
	DispositivoRegistro,
)


# Register your models here.
class DispositivoAdmin(admin.ModelAdmin):
	list_display=('tipo','updated',)

admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(DispositivoRegistro)