# Generated by Django 4.2.5 on 2025-01-22 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0058_profile_monday_friday_profile_saturday_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Office_time',
        ),
    ]
