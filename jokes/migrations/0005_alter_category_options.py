# Generated by Django 4.1.7 on 2023-04-10 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jokes", "0004_category_joke_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
