# Generated by Django 5.0.7 on 2024-08-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_remove_team_player_team_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.FileField(default=None, upload_to='news_post/')),
                ('capation', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]