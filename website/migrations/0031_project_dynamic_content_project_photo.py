# Generated by Django 4.2.5 on 2025-01-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_team_content_team_dynamic_content_delete_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_dynamic_content',
            name='project_photo',
            field=models.ImageField(blank=True, upload_to='web_photos'),
        ),
    ]
