# Generated by Django 5.0.4 on 2024-05-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_candidate_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
