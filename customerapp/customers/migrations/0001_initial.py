# Generated by Django 4.2.13 on 2024-05-23 03:36

import customers.models
from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=32, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=32, verbose_name="Last Name"),
                ),
                (
                    "address",
                    models.CharField(max_length=128, verbose_name="Street Address"),
                ),
                ("city", models.CharField(max_length=32, verbose_name="City")),
                (
                    "zip_code",
                    models.CharField(
                        max_length=5,
                        validators=[customers.models.validate_zip],
                        verbose_name="Zip Code",
                    ),
                ),
                (
                    "state",
                    localflavor.us.models.USStateField(
                        max_length=2, verbose_name="State"
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("first_name", "last_name", "address", "city", "zip_code", "state")
                },
            },
        ),
    ]
