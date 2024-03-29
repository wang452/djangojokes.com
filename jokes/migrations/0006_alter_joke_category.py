# Generated by Django 4.1.7 on 2023-04-10 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("jokes", "0005_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joke",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="jokes.category",
            ),
            preserve_default=False,
        ),
    ]
