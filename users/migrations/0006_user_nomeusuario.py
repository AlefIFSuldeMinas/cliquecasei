# Generated by Django 4.0.3 on 2022-06-14 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_grupousuario_user_celular_user_cep_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='NomeUsuario',
            field=models.TextField(blank=True),
        ),
    ]