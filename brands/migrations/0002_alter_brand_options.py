# Generated by Django 5.1 on 2024-09-12 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ('name',), 'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
    ]
