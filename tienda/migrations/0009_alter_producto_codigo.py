# Generated by Django 5.0.6 on 2024-07-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_remove_carro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Código'),
        ),
    ]
