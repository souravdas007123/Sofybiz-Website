# Generated by Django 4.2.4 on 2025-01-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_heading',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='sub_heading',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
