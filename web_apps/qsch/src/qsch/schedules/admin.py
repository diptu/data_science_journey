from django.contrib import admin
from .models import Schedule,Team,Shift


# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
        "is_on_non_paid_leave",
        "is_on_non_approved_leave",
        "is_on_paid_leave",
        "is_public_holiday",
        "is_on_sick_leave",
        "is_on_vacation",
        "is_weekend")

    list_display = ('employee', 'status', 'start_time', 'end_time', 'overtime_stated_at', 'overtime_ended_at')


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Team)
admin.site.register(Shift)
