# Generated by Django 4.0.6 on 2025-02-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0073_alter_service_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='query_data',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
