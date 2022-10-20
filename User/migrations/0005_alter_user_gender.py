# Generated by Django 4.1 on 2022-08-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0004_user_date_of_birth_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "Male"), ("female", "Female"), ("others", "Other")],
                default="",
                max_length=6,
            ),
        ),
    ]