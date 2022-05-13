from django.db import models
from employees.models import Employee
from django.utils.timezone import now
from django.core.exceptions import ValidationError

# Create your models here.
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

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('Start time should be before end time.')
        if self.overtime_stated_at > self.overtime_ended_at:
            raise ValidationError('Starting overtime should be before ending overtime.')
        if self.overtime_stated_at > self.end_time:
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
