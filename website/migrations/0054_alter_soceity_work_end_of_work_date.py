# Generated by Django 4.2.5 on 2025-01-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0053_delete_teximonial_dynamic_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soceity_work',
            name='end_of_work_date',
            field=models.DateField(),
        ),
    ]
