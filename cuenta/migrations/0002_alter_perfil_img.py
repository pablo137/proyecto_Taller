# Generated by Django 4.0 on 2023-05-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='img',
            field=models.ImageField(default='users/img_defecto_guzx7h.jpg', upload_to='users/', verbose_name='Imagen de perfil'),
        ),
    ]