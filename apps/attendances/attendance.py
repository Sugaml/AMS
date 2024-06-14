from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.models import *
from datetime import datetime
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Count, F
from django.db.models.functions import TruncDate
from datetime import datetime, date, timedelta



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
        return redirect('attendance/success')
    students = Student.objects.all()
    return render(request, 'attendances/attendance.html', {'students': students})
def AttendanceSuccess(request):
    return render(request, 'attendances/attendance_success.html')

def AttendanceReportView(request):
    # Retrieve today's date
    today_date = datetime.now().date()

    # Retrieve all attendance records for today
    attendance_records = Attendance.objects.filter(date=today_date).order_by('student')

    # Handling search based on student name
    student_name = request.GET.get('student_name')

    # Filter records based on student name if provided
    if student_name:
        attendance_records = attendance_records.filter(student__name__icontains=student_name)

     # Pagination
    paginator = Paginator(attendance_records, 10)  # Show 10 records per page
    page_number = request.GET.get('page')
    try:
        attendance_data = paginator.page(page_number)
    except PageNotAnInteger:
        attendance_data = paginator.page(1)
    except EmptyPage:
        attendance_data = paginator.page(paginator.num_pages)

    # Ensure attendance_data is not empty initially
    if not attendance_data:
        attendance_data = paginator.page(1)

    return render(request, 'attendances/attendance_report.html', {
        'attendance_data': attendance_data,
        'student_name': student_name  # Pass the searched student name back to the template
    })

def this_months_attendance_report(request):
    # Retrieve today's date
    today = date.today()

    # Calculate the first day of the current month
    first_day_of_month = today.replace(day=1)

    # Retrieve all attendance records for this month
    attendance_records = Attendance.objects.filter(
        date__gte=first_day_of_month
    ).order_by('date', 'student__name')

    # Handle search by student name
    student_name = request.GET.get('student_name')
    if student_name:
        attendance_records = attendance_records.filter(student__name__icontains=student_name)

    # Handle search by start date
    start_date = request.GET.get('start_date')
    if start_date:
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            attendance_records = attendance_records.filter(date__gte=start_date)
        except ValueError:
            pass

    # Handle search by end date
    end_date = request.GET.get('end_date')
    if end_date:
        try:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            end_date = end_date + timedelta(days=1)  # Adjust to include end date in the range
            attendance_records = attendance_records.filter(date__lt=end_date)
        except ValueError:
            pass

    # Aggregate total attendance counts per student
    attendance_counts = attendance_records.values('student__name').annotate(total_attendance=Count('id'))

    return render(request, 'attendances/this_months_attendance_report.html', {
        'attendance_counts': attendance_counts,
        'student_name': student_name,
        'start_date': start_date,
        'end_date': end_date,
        'today': today,  # Pass today's date to template for comparison
    })