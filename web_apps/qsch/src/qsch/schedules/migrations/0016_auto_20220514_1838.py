# Generated by Django 3.2.12 on 2022-05-14 18:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0015_auto_20220514_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='overtime_ended_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='overtime_stated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime, null=True),
        ),
    ]
