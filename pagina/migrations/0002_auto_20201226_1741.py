# Generated by Django 3.1.4 on 2020-12-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='plantilla',
            name='icono',
            field=models.ImageField(upload_to='icono_plantilla'),
        ),
        migrations.AlterField(
            model_name='plantilla',
            name='logo',
            field=models.ImageField(upload_to='logo_plantilla'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='img_fondo',
            field=models.ImageField(upload_to='img_fondo_slide'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='img_producto',
            field=models.ImageField(upload_to='img_producto_slide'),
        ),
    ]