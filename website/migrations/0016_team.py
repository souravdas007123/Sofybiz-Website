# Generated by Django 4.2.4 on 2025-01-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_project_project_heading_project_sub_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_heading', models.CharField(default=0, max_length=200)),
                ('sub_heading', models.CharField(default=0, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
    ]
