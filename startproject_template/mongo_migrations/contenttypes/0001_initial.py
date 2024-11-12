# Generated by Django 5.0.9 on 2024-10-04 20:15

import django.contrib.contenttypes.models
import django_mongodb.fields.auto
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContentType",
            fields=[
                (
                    "id",
                    django_mongodb.fields.auto.ObjectIdAutoField(
                        auto_created=True,
                        db_column="_id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                (
                    "model",
                    models.CharField(
                        max_length=100, verbose_name="python model class name"
                    ),
                ),
            ],
            options={
                "verbose_name": "content type",
                "verbose_name_plural": "content types",
                "db_table": "django_content_type",
                "unique_together": {("app_label", "model")},
            },
            managers=[
                ("objects", django.contrib.contenttypes.models.ContentTypeManager()),
            ],
        ),
    ]
