# Generated by Django 4.2.5 on 2025-01-21 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0054_alter_soceity_work_end_of_work_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project_dynamic_content',
        ),
        migrations.RemoveField(
            model_name='contact_content',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contact_content',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact_content',
            name='mobile_no',
        ),
    ]
