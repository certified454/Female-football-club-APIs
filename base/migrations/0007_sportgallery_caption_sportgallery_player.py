# Generated by Django 5.0.7 on 2024-08-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_sportgallery_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportgallery',
            name='caption',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='sportgallery',
            name='player',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
