# Generated by Django 3.1.7 on 2021-02-27 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_espaco_sala'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaSala',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('id_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.sala')),
                ('pessoa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.pessoa')),
            ],
            options={
                'db_table': 'reserva_sala',
            },
        ),
        migrations.CreateModel(
            name='ReservaEspaco',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('id_espaco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.espaco')),
                ('pessoa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.pessoa')),
            ],
            options={
                'db_table': 'reserva_espaço',
            },
        ),
    ]
