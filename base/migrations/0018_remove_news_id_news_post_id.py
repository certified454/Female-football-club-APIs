# Generated by Django 5.0.7 on 2024-08-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='id',
        ),
        migrations.AddField(
            model_name='news',
            name='post_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]