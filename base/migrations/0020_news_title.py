# Generated by Django 5.0.7 on 2024-08-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_remove_news_post_id_news_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default=None, max_length=10),
        ),
    ]