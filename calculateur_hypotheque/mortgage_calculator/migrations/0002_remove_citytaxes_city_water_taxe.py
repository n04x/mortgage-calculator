# Generated by Django 3.0.7 on 2020-06-29 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage_calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citytaxes',
            name='city_water_taxe',
        ),
    ]
