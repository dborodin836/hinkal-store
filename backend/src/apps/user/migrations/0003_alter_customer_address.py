# Generated by Django 4.1.7 on 2023-03-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_remove_useraddress_county_delete_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="address",
            field=models.CharField(max_length=256, null=True),
        ),
    ]
