# Generated by Django 4.0.3 on 2022-06-21 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convite', '0004_alter_convitecasamento_fotocasal'),
    ]

    operations = [
        migrations.AddField(
            model_name='convitecasamento',
            name='IdUsuario',
            field=models.IntegerField(default=0),
        ),
    ]
