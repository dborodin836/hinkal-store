# Generated by Django 4.1.7 on 2023-03-31 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0003_delete_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
    ]