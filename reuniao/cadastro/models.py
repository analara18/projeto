from django.db import models

class Pessoa(models.Model):
	id_pessoa = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	sobrenome = models.CharField(max_length=100)

	class Meta:
		db_table = "pessoa"




