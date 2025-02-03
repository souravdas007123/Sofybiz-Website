# Generated by Django 4.2.5 on 2025-01-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_rename_totalwork_soceity_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_heading', models.CharField(default=0, max_length=200)),
                ('sub_heading', models.CharField(default=0, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project_dynamic_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
