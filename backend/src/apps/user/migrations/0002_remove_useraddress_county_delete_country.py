# Generated by Django 4.1.7 on 2023-03-31 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useraddress",
            name="county",
        ),
        migrations.DeleteModel(
            name="Country",
        ),
    ]
