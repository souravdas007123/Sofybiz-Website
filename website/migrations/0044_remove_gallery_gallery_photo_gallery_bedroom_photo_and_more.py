# Generated by Django 4.2.5 on 2025-01-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0043_teximonial_dynamic_content_company_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='gallery_photo',
        ),
        migrations.AddField(
            model_name='gallery',
            name='bedroom_photo',
            field=models.ImageField(default=0, upload_to='web_photos'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='drawingroom_photo',
            field=models.ImageField(default=0, upload_to='web_photos'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='falseceilling_photo',
            field=models.ImageField(default=0, upload_to='web_photos'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='kitchen_photo',
            field=models.ImageField(default=0, upload_to='web_photos'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='lighting_photo',
            field=models.ImageField(default=0, upload_to='web_photos'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='livingroom_photo',
            field=models.ImageField(default=0, upload_to='web_photos'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='tiles_photo',
            field=models.ImageField(default=0, upload_to='web_photos'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='wallpannel_photo',
            field=models.ImageField(default=0, upload_to='web_photos'),
        ),
    ]
