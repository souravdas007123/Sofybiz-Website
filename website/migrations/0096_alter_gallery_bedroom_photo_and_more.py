# Generated by Django 4.0.6 on 2025-02-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0095_alter_about_options_alter_achivement_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='bedroom_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='drawingroom_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='falseceilling_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='floor_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='kitchen_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='livingroom_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='wallpannel_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='washroom_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
    ]
