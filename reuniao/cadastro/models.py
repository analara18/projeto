from django.db import models

class Pessoa(models.Model):
	id_pessoa = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	sobrenome = models.CharField(max_length=100)

	class Meta:
		db_table = "pessoa"


class Sala(models.Model):
	id_sala = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	lotacao = models.IntegerField()

	class Meta:
		db_table = "sala"


class Espaco(models.Model):
	id_espaco = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	lotacao = models.IntegerField()
	
	class Meta:
		db_table = "espaco"


class ReservaSala(models.Model):
	id_reserva = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
	
	class Meta:
		db_table = "reserva_sala"


class ReservaSalaPessoa(models.Model):
	id_reserva_pessoa = models.AutoField(primary_key=True)
	pessoa_id = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	id_reserva = models.ForeignKey(ReservaSala, on_delete=models.CASCADE)
	
	class Meta:
		db_table = "reserva_sala_pessoa"


class ReservaEspaco(models.Model):
	id_reserva = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	pessoa_id = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	id_espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
	
	class Meta:
		db_table = "reserva_espaço"


