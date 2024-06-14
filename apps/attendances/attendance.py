from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.models import *
from datetime import datetime
from datetime import date
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.db.models import Count, F
from django.db.models.functions import TruncDate


def AttendanceView(request):
    today = date.today()
    if Attendance.objects.filter(date=today).exists():
        return redirect('attendance_report')

    if request.method == 'POST':
        for student_id, status in request.POST.items():
            if student_id.startswith('student_'):
                student_id = student_id.split('_')[1]
                student = Student.objects.get(pk=student_id)
                if not Attendance.objects.filter(student=student, date=today).exists():
                    Attendance.objects.create(student=student, date=today, status=status)
        return redirect('attendance-success')
    students = Student.objects.all()
    return render(request, 'apps/attendance.html', {'students': students})

def AttendanceSuccess(request):
    return render(request, 'apps/attendance_success.html')

def AttendanceReportView(request):
    attendance_records = Attendance.objects.all().order_by('date', 'student')
    return render(request, 'apps/attendance_report.html', {'attendance_records': attendance_records})

    
def MonitoringReportView(request):
    current_month = datetime.now().month
    current_year = datetime.now().year

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        attendance_data = Attendance.objects.filter(date__range=[start_date, end_date]).values('student__name').annotate(total_attendance=Count('id'), total_days=Count(TruncDate('date'), distinct=True))
    else:
        attendance_data = Attendance.objects.filter(date__month=current_month, date__year=current_year).values('student__name').annotate(total_attendance=Count('id'), total_days=Count(TruncDate('date'), distinct=True))

    return render(request, 'apps/attendance-month.html', {'attendance_data': attendance_data})