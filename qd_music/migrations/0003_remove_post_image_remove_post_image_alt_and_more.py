# Generated by Django 4.0.4 on 2022-06-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qd_music', '0002_remove_post_author_post_cover_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_alt',
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=200, null='true', unique=True),
            preserve_default='true',
        ),
    ]
