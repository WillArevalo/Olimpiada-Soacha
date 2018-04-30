from django import forms
from registros.models import DispositivoRegistro
#form en vista de detalle y en vista de crear un comentario
class RegisterForm(forms.ModelForm):

	class Meta:
		model = DispositivoRegistro
		fields = [
			'dispositivo',
			'estudiante',
			'cantidad',
			'estado',
			'devuelto',
		]