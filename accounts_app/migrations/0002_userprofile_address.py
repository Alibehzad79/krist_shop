# Generated by Django 5.1.4 on 2024-12-10 07:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Phone Number"
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        upload_to="profiles/images/", verbose_name="Profile Image"
                    ),
                ),
                (
                    "profile_bg_image",
                    models.ImageField(
                        upload_to="profiles/images/",
                        verbose_name="Profile Background Image",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
            },
        ),
        migrations.CreateModel(
            name="Address",
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
                    "phone_number",
                    models.CharField(max_length=50, verbose_name="Phone Number"),
                ),
                ("country", models.CharField(max_length=50, verbose_name="Country")),
                ("city", models.CharField(max_length=50, verbose_name="City")),
                ("state", models.CharField(max_length=100, verbose_name="State")),
                ("zip_code", models.CharField(max_length=50, verbose_name="Zip Code")),
                ("more_info", models.TextField(verbose_name="More Info")),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="accounts_app.userprofile",
                        verbose_name="Prifle",
                    ),
                ),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
            },
        ),
    ]