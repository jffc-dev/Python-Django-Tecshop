# Generated by Django 3.1.5 on 2021-01-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0017_auto_20210118_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen_promocion',
            field=models.ImageField(default=1, upload_to='categorias_promo'),
            preserve_default=False,
        ),
    ]
