# Generated by Django 5.0.7 on 2024-08-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_joinform_date_of_birth_alter_joinform_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinform',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
