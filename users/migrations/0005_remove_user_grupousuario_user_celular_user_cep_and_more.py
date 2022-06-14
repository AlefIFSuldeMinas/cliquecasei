# Generated by Django 4.0.3 on 2022-06-13 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_grupousuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='GrupoUsuario',
        ),
        migrations.AddField(
            model_name='user',
            name='Celular',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Cep',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Cidade',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Endereco',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Estado',
            field=models.TextField(blank=True),
        ),
    ]
