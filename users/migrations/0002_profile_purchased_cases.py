# Generated by Django 5.1.5 on 2025-02-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='purchased_cases',
            field=models.JSONField(default=dict),
        ),
    ]
