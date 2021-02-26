from django import forms

from cadastro.models import Pessoa, Sala, Espaco

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = '__all__'

class SalaForm(forms.ModelForm):
	class Meta:
		model = Sala
		fields = '__all__'

class EspacoForm(forms.ModelForm):
	class Meta:
		model = Espaco
		fields = '__all__'

