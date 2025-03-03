# Generated by Django 4.2.5 on 2025-01-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0055_delete_project_dynamic_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landing_heading', models.CharField(max_length=200)),
                ('contact_heading', models.CharField(default=0, max_length=200)),
                ('contact_para', models.CharField(default=0, max_length=200)),
                ('service_heading', models.CharField(default=0, max_length=200)),
                ('service_para', models.CharField(default=0, max_length=200)),
                ('milestone_heading', models.CharField(default=0, max_length=200)),
                ('milestone_para', models.CharField(default=0, max_length=200)),
                ('project_heading', models.CharField(default=0, max_length=200)),
                ('project_para', models.CharField(default=0, max_length=200)),
                ('gallery_heading', models.CharField(default=0, max_length=200)),
                ('gallery_para', models.CharField(default=0, max_length=200)),
                ('team_heading', models.CharField(default=0, max_length=200)),
                ('team_para', models.CharField(default=0, max_length=200)),
                ('teximonial_heading', models.CharField(default=0, max_length=200)),
                ('teximonial_para', models.CharField(default=0, max_length=200)),
                ('achivement_heading', models.CharField(default=0, max_length=200)),
                ('achivement_para', models.CharField(default=0, max_length=200)),
                ('about_heading', models.CharField(default=0, max_length=200)),
                ('about_para', models.CharField(default=0, max_length=200)),
            ],
        ),
    ]
