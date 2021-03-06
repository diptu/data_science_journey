# Generated by Django 3.2.12 on 2022-05-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.CharField(blank=True, choices=[('Non Paid Leave', 'Non Paid Leave'), ('Leave (non-approved)', 'Leave (non-approved)'), ('Paid Leave', 'Paid Leave'), ('Public Holiday', 'Public Holiday'), ('Sick Leave', 'Sick Leave'), ('Vacation', 'Vacation'), ('Weekend', 'Weekend')], default=None, max_length=20, null=True),
        ),
    ]
