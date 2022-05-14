from django.urls import path
from .views import ScheduleLisit,ScheduleDetailView,ScheduleCreateView,ScheduleUpdateView,ScheduleDeleteView
app_name = "Schedules"
urlpatterns = [

    path('',ScheduleLisit.as_view(),name="schedule-list"),
    path('create/', ScheduleCreateView.as_view(), name="schedule-create"),
    path('<int:pk>/', ScheduleDetailView.as_view(), name="schedule-detail"),
    path('<int:pk>/update/', ScheduleUpdateView.as_view(), name="schedule-update"),
    path('<int:pk>/delete/', ScheduleDeleteView.as_view(), name="schedule-delete"),

]