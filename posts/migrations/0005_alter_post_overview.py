# Generated by Django 4.1.5 on 2023-01-08 19:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post", name="overview", field=tinymce.models.HTMLField(),
        ),
    ]
