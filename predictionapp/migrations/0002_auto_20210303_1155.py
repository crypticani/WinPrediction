# Generated by Django 3.1.7 on 2021-03-03 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamregistrationmodel',
            name='year',
            field=models.DateField(default=datetime.datetime(2021, 3, 3, 11, 55, 23, 634132)),
        ),
    ]
