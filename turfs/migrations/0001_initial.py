# Generated by Django 5.1.1 on 2024-09-17 09:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Forget_turf_password",
            fields=[
                ("user_name", models.CharField(max_length=20)),
                (
                    "mobile_number",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("mailid", models.EmailField(max_length=50, unique=True)),
                ("otp", models.CharField(max_length=6)),
                ("isvalid", models.CharField(default="True", max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Turf_registration",
            fields=[
                ("turf_name", models.CharField(max_length=50)),
                ("turf_address", models.CharField(max_length=500)),
                ("turf_pincode", models.CharField(max_length=6)),
                (
                    "turf_mobile_number",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("turf_mailid", models.EmailField(max_length=50, unique=True)),
                ("turf_land_line_number", models.CharField(max_length=20, null=True)),
                ("turf_images_path", models.JSONField(max_length=1000)),
                (
                    "registration_date",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("user_name", models.CharField(max_length=20, unique=True)),
                ("password", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Random_token_generation",
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
                ("user_name", models.CharField(max_length=20, unique=True)),
                ("random_token", models.CharField(max_length=200)),
                (
                    "turf_mobile_number",
                    models.ForeignKey(
                        default="0000000000",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="turfs.turf_registration",
                    ),
                ),
            ],
        ),
    ]