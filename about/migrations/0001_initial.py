# Generated by Django 4.1.5 on 2023-02-16 12:56

import about.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import json.decoder
import json.encoder


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageModel",
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
                ("club", models.CharField(max_length=10)),
                ("image", models.FileField(null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="ClubModel",
            fields=[
                ("name", models.CharField(default="테스트_동아리", max_length=100)),
                (
                    "code",
                    models.CharField(
                        default="test_club",
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("form_start", models.DateTimeField(default=datetime.datetime.now)),
                ("form_end", models.DateTimeField(default=datetime.datetime.now)),
                ("index_banner_description", models.TextField(default="동아리 소개 준비중")),
                (
                    "about_text",
                    models.TextField(default="# 동아리 소개 준비중\n동아리에서 아직 내용을 준비하는 중이에요."),
                ),
                (
                    "form_data",
                    models.JSONField(
                        decoder=json.decoder.JSONDecoder,
                        default=about.models.form_data_default,
                        encoder=json.encoder.JSONEncoder,
                    ),
                ),
                ("form_edit_url", models.URLField(blank=True, null=True)),
                (
                    "about_background",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="about_background+",
                        to="about.imagemodel",
                    ),
                ),
                (
                    "about_images",
                    models.ManyToManyField(
                        blank=True, related_name="about_images+", to="about.imagemodel"
                    ),
                ),
                (
                    "index_banner_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="index_banner_image+",
                        to="about.imagemodel",
                    ),
                ),
                (
                    "logo_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="logo_image+",
                        to="about.imagemodel",
                    ),
                ),
            ],
        ),
    ]
