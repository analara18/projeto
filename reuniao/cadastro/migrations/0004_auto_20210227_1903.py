# Generated by Django 3.1.7 on 2021-02-27 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_reservaespaco_reservasala'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservasala',
            name='pessoa_id',
        ),
        migrations.CreateModel(
            name='ReservaSalaPessoa',
            fields=[
                ('id_reserva_pessoa', models.AutoField(primary_key=True, serialize=False)),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.reservasala')),
                ('pessoa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.pessoa')),
            ],
            options={
                'db_table': 'reserva_sala_pessoa',
            },
        ),
    ]