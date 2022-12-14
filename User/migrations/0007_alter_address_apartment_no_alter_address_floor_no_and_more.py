# Generated by Django 4.1 on 2022-09-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0006_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="apartment_no",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="floor_no",
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="street_address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
