# Generated by Django 5.1.5 on 2025-02-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0070_service_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_caterory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=400)),
            ],
        ),
    ]
