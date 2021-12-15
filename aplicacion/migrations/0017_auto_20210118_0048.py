# Generated by Django 3.1.5 on 2021-01-18 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0016_auto_20210116_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoria',
            name='icono',
            field=models.CharField(default='icono', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deseo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deseos', to='aplicacion.usuario'),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='aplicacion.compra'),
        ),
    ]