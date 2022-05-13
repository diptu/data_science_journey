# Generated by Django 3.2.12 on 2022-05-13 18:34

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0006_auto_20220509_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('D', 'Day'), ('N', 'Night'), ('E', 'Evening')], default='D', help_text='Day Shift 5 day 40 hours', max_length=1)),
                ('weekly_contracted_man_hour', models.DurationField(default=datetime.timedelta(days=1, seconds=57600), verbose_name='Contracted Man Hours per week')),
                ('shift_per_week', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='No of shift per week')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_group', models.CharField(help_text='Group Name- Group No i,e Alhpa-0', max_length=20)),
                ('group', models.CharField(help_text='Group Name i,e Alhpa', max_length=20)),
                ('operation', models.CharField(max_length=20)),
            ],
        ),
    ]