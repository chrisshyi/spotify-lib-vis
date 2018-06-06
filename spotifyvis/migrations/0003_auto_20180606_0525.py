# Generated by Django 2.0.5 on 2018-06-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifyvis', '0002_auto_20180606_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofeatures',
            name='loudness',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='audiofeatures',
            name='tempo',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
