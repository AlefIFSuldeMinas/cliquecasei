# Generated by Django 4.0.3 on 2022-06-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convite', '0002_alter_convidados_acompanhantes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convidados',
            name='Acompanhantes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='convidados',
            name='NomeConvidado',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='convidados',
            name='Observacoes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='convidados',
            name='TelefoneConvidado',
            field=models.TextField(blank=True),
        ),
    ]