# Generated by Django 5.0.4 on 2024-05-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_employer'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='hr_email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
