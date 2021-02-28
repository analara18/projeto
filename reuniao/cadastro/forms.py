from django import forms

from cadastro.models import Pessoa, Sala, Espaco, ReservaSala, ReservaSalaPessoa

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


class ReservaSalaForm(forms.ModelForm):
	class Meta:
		model = ReservaSala
		fields = '__all__'


class ReservaSalaPessoaForm(forms.ModelForm):
	class Meta:
		model = ReservaSalaPessoa
		fields = '__all__'
