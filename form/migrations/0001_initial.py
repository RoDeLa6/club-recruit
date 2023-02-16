# Generated by Django 4.1.5 on 2023-02-16 12:56

from django.db import migrations, models
import django.db.models.deletion
import json.decoder
import json.encoder


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormModel",
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
                ("number", models.IntegerField()),
                (
                    "section",
                    models.JSONField(
                        decoder=json.decoder.JSONDecoder,
                        encoder=json.encoder.JSONEncoder,
                    ),
                ),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="about.clubmodel",
                    ),
                ),
            ],
        ),
    ]
