# Generated by Django 4.1 on 2022-10-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0006_alter_orderitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="shipment_id",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
