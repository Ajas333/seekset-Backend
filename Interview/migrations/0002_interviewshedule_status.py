# Generated by Django 5.0.4 on 2024-06-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewshedule',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
