# Generated by Django 4.2.5 on 2025-01-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_employee_work_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_friday', models.CharField(max_length=100)),
                ('saturday', models.CharField(max_length=100)),
                ('sunday', models.CharField(max_length=100)),
            ],
        ),
    ]
