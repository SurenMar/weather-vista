# Generated by Django 5.2.1 on 2025-05-27 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_monthlyweather_avg_temp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyweather',
            name='gust_speed',
        ),
        migrations.RemoveField(
            model_name='monthlyweather',
            name='snow_depth',
        ),
        migrations.RemoveField(
            model_name='monthlyweather',
            name='sunshine',
        ),
    ]
