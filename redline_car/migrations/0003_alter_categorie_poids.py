# Generated by Django 3.2.5 on 2022-08-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redline_car', '0002_vehicule_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='poids',
            field=models.IntegerField(),
        ),
    ]
