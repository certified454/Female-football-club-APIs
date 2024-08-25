# Generated by Django 5.0.7 on 2024-08-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_rename_name_team_team_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_logo', models.ImageField(default=None, upload_to='team_logo/')),
                ('venue', models.CharField(max_length=50)),
                ('kickoff', models.CharField(max_length=20)),
                ('date_schedule', models.CharField(max_length=20)),
            ],
        ),
    ]