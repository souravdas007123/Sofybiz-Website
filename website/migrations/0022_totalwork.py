# Generated by Django 4.2.5 on 2025-01-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_landing_content_landing_dynamic_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Totalwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('sub_work', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
    ]
