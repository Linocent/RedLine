# Generated by Django 3.2.5 on 2022-08-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redline_car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='thumbnail',
            field=models.FilePathField(default=None),
            preserve_default=False,
        ),
    ]
