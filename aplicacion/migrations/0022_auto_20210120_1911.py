# Generated by Django 3.1.5 on 2021-01-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0021_auto_20210120_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios'),
        ),
    ]