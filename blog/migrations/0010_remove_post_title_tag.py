# Generated by Django 3.2.21 on 2024-01-05 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_image_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
    ]
