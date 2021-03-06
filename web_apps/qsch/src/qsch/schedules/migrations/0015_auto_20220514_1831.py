# Generated by Django 3.2.12 on 2022-05-14 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0014_auto_20220514_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 14, 18, 31, 54, 275639), null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='overtime_ended_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 14, 18, 31, 54, 275651), null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='overtime_stated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 14, 18, 31, 54, 275646), null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 14, 18, 31, 54, 275626), null=True),
        ),
    ]
