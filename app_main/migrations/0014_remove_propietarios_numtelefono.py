# Generated by Django 4.1.7 on 2023-04-10 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0013_propietarios_numtelefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propietarios',
            name='numTelefono',
        ),
    ]