# Generated by Django 4.1.7 on 2023-03-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0003_remove_consumidor_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumidor',
            name='img_perfil',
            field=models.ImageField(default='default1.png', upload_to=''),
        ),
    ]