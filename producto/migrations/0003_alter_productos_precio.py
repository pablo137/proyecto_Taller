# Generated by Django 4.0 on 2023-05-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_alter_categorias_img_alter_productos_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]