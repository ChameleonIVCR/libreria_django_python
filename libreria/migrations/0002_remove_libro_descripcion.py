# Generated by Django 3.2.7 on 2021-09-02 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='descripcion',
        ),
    ]
