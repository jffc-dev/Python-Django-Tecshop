# Generated by Django 3.1.5 on 2021-01-15 04:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0010_auto_20210113_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='cantidad',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='aplicacion.producto'),
        ),
    ]