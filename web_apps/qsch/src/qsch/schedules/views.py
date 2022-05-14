from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,ModelFormMixin
from .models import Schedule
# Create your views here.

class ScheduleLisit(ListView):
    model = Schedule
    """
        A hyphen "-" in front of "start_time" indicates descending order
    """
    queryset = Schedule.objects.order_by('-start_time')

class ScheduleDetailView(DetailView):
    model = Schedule

class ScheduleCreateView(CreateView):
    model = Schedule
    fields = ['employee', 'status', 'start_time', 'end_time', 'overtime_stated_at', 'overtime_ended_at']
    success_url = '../'

class ScheduleUpdateView(UpdateView):
    model = Schedule
    fields = ['employee', 'status', 'start_time', 'end_time', 'overtime_stated_at', 'overtime_ended_at']
    template_name_suffix = '_update_form'
    success_url = '/schedule/'

class ScheduleDeleteView(DeleteView):
    model = Schedule
    success_url = reverse_lazy('Schedules:schedule-list')