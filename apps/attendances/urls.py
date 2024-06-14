from django.urls import path
from . import attendance as views


urlpatterns = [
    path('', views.AttendanceView, name='attendance_view'),
    path('report/', views.AttendanceReportView, name='attendance_report'),
    path('success/', views.AttendanceSuccess, name='attendance_success'),
    path('monitoring-report/', views.MonitoringReportView, name='monitoring_report_view'),
]