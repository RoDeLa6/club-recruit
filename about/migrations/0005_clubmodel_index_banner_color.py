# Generated by Django 4.1.5 on 2023-02-27 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0004_alter_clubmodel_kakao_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="clubmodel",
            name="index_banner_color",
            field=models.CharField(default="#000000", max_length=7),
        ),
    ]
