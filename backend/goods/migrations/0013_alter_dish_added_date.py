# Generated by Django 4.0.3 on 2022-04-27 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0012_alter_dish_added_by_alter_dish_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 17, 54, 29, 680135), verbose_name='Added'),
        ),
    ]