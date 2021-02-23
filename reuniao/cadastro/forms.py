from django import forms

from cadastro.models import Pessoa

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = '__all__'
