# Generated by Django 5.0.7 on 2024-08-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_sportgallery_caption_sportgallery_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportgallery',
            name='caption',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sportgallery',
            name='player',
            field=models.CharField(max_length=50),
        ),
    ]