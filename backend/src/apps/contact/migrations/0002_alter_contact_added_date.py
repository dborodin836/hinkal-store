# Generated by Django 4.0.4 on 2022-04-29 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 29, 1, 4, 56, 374543)),
        ),
    ]