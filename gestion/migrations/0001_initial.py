# Generated by Django 5.1.7 on 2025-03-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
