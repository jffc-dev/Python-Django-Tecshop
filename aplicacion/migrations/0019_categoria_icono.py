# Generated by Django 3.1.5 on 2021-01-19 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0018_categoria_imagen_promocion'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='icono',
            field=models.CharField(default='icono', max_length=100),
            preserve_default=False,
        ),
    ]
