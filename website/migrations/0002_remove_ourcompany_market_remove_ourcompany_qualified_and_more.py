# Generated by Django 4.2.4 on 2025-01-03 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourcompany',
            name='market',
        ),
        migrations.RemoveField(
            model_name='ourcompany',
            name='qualified',
        ),
        migrations.RemoveField(
            model_name='ourcompany',
            name='staff',
        ),
        migrations.AlterField(
            model_name='ourcompany',
            name='implemented',
            field=models.CharField(max_length=70),
        ),
    ]
