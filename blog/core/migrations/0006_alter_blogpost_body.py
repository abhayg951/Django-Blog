# Generated by Django 5.0.1 on 2024-02-24 12:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_blogpost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
