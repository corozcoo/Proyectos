# Generated by Django 3.2.6 on 2021-09-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210916_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.CharField(choices=[('D', 'DPI'), ('C', 'CEDULA')], default='C', max_length=20),
        ),
    ]
