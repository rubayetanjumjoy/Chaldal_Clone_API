# Generated by Django 4.1 on 2022-09-07 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0013_alter_address_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
