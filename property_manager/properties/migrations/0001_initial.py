# Generated by Django 4.1.1 on 2022-10-13 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SingleProperty",
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
                ("address", models.CharField(max_length=200)),
                ("unit", models.IntegerField()),
                ("city", models.CharField(max_length=200)),
                ("zip_code", models.CharField(max_length=10)),
                ("type", models.CharField(max_length=200)),
                ("status", models.CharField(max_length=100)),
                ("bedrooms", models.IntegerField()),
                ("price", models.FloatField()),
                ("baths", models.IntegerField()),
                ("square_feet", models.FloatField()),
                ("year_built", models.IntegerField()),
                ("pets", models.BooleanField()),
                (
                    "realtor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="realtor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tenant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="tenant",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]