# Generated by Django 5.1.6 on 2025-03-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_rest_app', '0003_show_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='dull'),
            preserve_default=False,
        ),
    ]
