# Generated by Django 5.0.6 on 2024-06-27 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usario',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('clave', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
    ]