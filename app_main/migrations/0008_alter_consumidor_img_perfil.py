# Generated by Django 4.1.7 on 2023-03-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0007_alter_emprendedor_img_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumidor',
            name='img_perfil',
            field=models.ImageField(null=True, upload_to='consumidores'),
        ),
    ]