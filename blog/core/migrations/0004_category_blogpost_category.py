# Generated by Django 5.0.1 on 2024-02-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_blogpost_created_at_alter_blogpost_title_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
