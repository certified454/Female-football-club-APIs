# Generated by Django 5.0.7 on 2024-08-20 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_team_team_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='team_name',
        ),
    ]