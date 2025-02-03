# Generated by Django 4.2.5 on 2025-01-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_office_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', models.CharField(max_length=300)),
                ('vision_img', models.ImageField(upload_to='web_photos')),
                ('Inspire', models.CharField(max_length=300)),
                ('Inspire_img', models.ImageField(upload_to='web_photos')),
                ('Dreams', models.CharField(max_length=300)),
                ('Dreams_img', models.ImageField(upload_to='web_photos')),
            ],
        ),
    ]
