# Generated by Django 3.1.4 on 2020-12-21 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('titulo1', models.CharField(max_length=100)),
                ('titulo2', models.CharField(max_length=100)),
                ('titulo3', models.CharField(max_length=100)),
                ('estilo', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barra_superior', models.CharField(max_length=200)),
                ('texto_superior', models.CharField(max_length=100)),
                ('color_fondo', models.CharField(max_length=100)),
                ('color_texto', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=100)),
                ('icono', models.CharField(max_length=100)),
                ('redes_sociales', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_fondo', models.CharField(max_length=100)),
                ('tipo_slide', models.CharField(max_length=100)),
                ('img_producto', models.CharField(max_length=100)),
                ('estilo_img_producto', models.CharField(max_length=100)),
                ('estilo_texto_slide', models.CharField(max_length=100)),
                ('titulo1', models.CharField(max_length=100)),
                ('titulo2', models.CharField(max_length=100)),
                ('titulo3', models.CharField(max_length=100)),
                ('boton', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
