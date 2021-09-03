# Generated by Django 3.2.7 on 2021-09-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=800)),
                ('genero', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=200)),
                ('publicacion', models.DateField()),
            ],
        ),
    ]