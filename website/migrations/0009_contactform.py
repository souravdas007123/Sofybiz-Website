# Generated by Django 4.2.4 on 2025-01-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_term_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=200)),
                ('email', models.EmailField(default=0, max_length=200)),
                ('address', models.CharField(default=0, max_length=70)),
                ('category', models.CharField(default=0, max_length=200)),
            ],
        ),
    ]
