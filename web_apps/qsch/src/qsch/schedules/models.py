from django.db import models
from django.urls import reverse
from employees.models import Employee
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta


# Create your models here.

class Shift(models.Model):
    DAY = 'D'
    NIGHT = 'N'
    EVENING = 'E'

    SHIFT_CHOICES = (
        (DAY, 'Day'),
        (NIGHT, "Night"),
        (EVENING, 'Evening'),
    )
    shift = models.CharField(max_length=1, choices=SHIFT_CHOICES, default=DAY,
                             help_text='Day Shift 5 day 40 hours')
    name = models.CharField(max_length=30, help_text='Day Shift 5 day 40 hours')
    weekly_contracted_man_hour = models.DurationField(verbose_name='Contracted Man Hours per week',
                                                      default=timedelta(hours=40))
    shift_per_week = models.IntegerField(verbose_name='No of shift per week', default=5,
                                         validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class Team(models.Model):
    sub_group = models.CharField(max_length=20, help_text='Group Name-Group No i,e Alhpa-0')
    group = models.CharField(max_length=20, help_text='Group Name i,e Alhpa')

    BANGLADESH = 'BD'
    UKRAINE = 'UA'
    SERBIA = 'RS'

    OPERATION_CHOICES = (
        (BANGLADESH, 'Bangladesh'),
        (UKRAINE, 'Ukraine'),
        (SERBIA, 'Serbia'),
    )
    operation = models.CharField(max_length=2, choices=OPERATION_CHOICES, default=BANGLADESH)
    sub_group_lead = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                       related_name='sub_group_lead')
    group_lead = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='group_lead')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    @property
    def sub_group_leader(self):
        return self.sub_group_lead.slug

    @property
    def group_leader(self):
        return self.group_lead.slug

    @property
    def shift(self):
        return self.shift.name
    def __str__(self):
        return self.sub_group

class Schedule(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Employee",
    )
    NON_PAID_LEAVE = 'on Paid Leave'
    NON_APPROVED_LEAVE = 'Leave (non-approved)'
    PAID_LEAVE = 'Paid Leave'
    PUBLIC_HOLIDAY = 'Public Holiday'
    SICK_LEAVE = 'Sick Leave'
    VACATION = 'Vacation'
    WEEKEND = 'Weekend'

    CHOICES = (
        (NON_PAID_LEAVE, 'Non Paid Leave'),
        (NON_APPROVED_LEAVE, 'Leave (non-approved)'),
        (PAID_LEAVE, 'Paid Leave'),
        (PUBLIC_HOLIDAY, 'Public Holiday'),
        (SICK_LEAVE, 'Sick Leave'),
        (VACATION, 'Vacation'),
        (WEEKEND, 'Weekend'),
    )

    status = models.CharField(max_length=20, choices=CHOICES, default=None, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True, default=now)
    end_time = models.DateTimeField(blank=True, null=True, default=now)
    overtime_stated_at = models.DateTimeField(blank=True, null=True, default=now)
    overtime_ended_at = models.DateTimeField(blank=True, null=True, default=now)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)

    is_on_non_paid_leave = models.BooleanField(default=False)
    is_on_non_approved_leave = models.BooleanField(default=False)
    is_on_paid_leave = models.BooleanField(default=False)
    is_public_holiday = models.BooleanField(default=False)
    is_on_sick_leave = models.BooleanField(default=False)
    is_on_vacation = models.BooleanField(default=False)
    is_weekend = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.employee)

    @property
    def get_emp(self):
        return self.employee.slug
    @property
    def get_email(self):
        return self.employee.email

    @property
    def get_operations(self):
        return self.team.operation

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('Start time should be before end time.')
        if self.overtime_stated_at > self.overtime_ended_at:
            raise ValidationError('Starting overtime should be before ending overtime.')
        if self.overtime_stated_at < self.end_time:
            raise ValidationError('Regular end time should be before starting overtime.')

    def save(self, *args, **kwargs):

        self.is_on_non_paid_leave = 1 if self.status == self.NON_PAID_LEAVE else 0
        self.is_on_non_approved_leave = 1 if self.status == self.NON_APPROVED_LEAVE else 0
        self.is_on_paid_leave = 1 if self.status == self.PAID_LEAVE else 0
        self.is_public_holiday = 1 if self.status == self.PUBLIC_HOLIDAY else 0
        self.is_on_sick_leave = 1 if self.status == self.SICK_LEAVE else 0
        self.is_on_vacation = 1 if self.status == self.VACATION else 0
        self.is_weekend = 1 if self.status == self.WEEKEND else 0

        super(Schedule, self).save(*args, **kwargs)
