# Generated by Django 4.1.7 on 2023-04-11 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0002_rename_application_applicant"),
    ]

    operations = [
        migrations.RenameField(
            model_name="applicant",
            old_name="available_date",
            new_name="available_days",
        ),
    ]