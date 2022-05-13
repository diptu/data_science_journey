# Generated by Django 3.2.12 on 2022-05-13 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_alter_employee_email'),
        ('schedules', '0008_auto_20220513_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='group_lead',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group_lead', to='employees.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='sub_group_lead',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sub_group_lead', to='employees.employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='sub_group',
            field=models.CharField(help_text='Group Name-Group No i,e Alhpa-0', max_length=20),
        ),
    ]
