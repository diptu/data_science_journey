from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)