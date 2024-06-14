from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Attendance
from datetime import date


def attendance_view(request):
    if request.method == 'POST':
        for student_id, status in request.POST.items():
            if student_id.startswith('student_'):
                student_id = student_id.split('_')[1]
                student = Student.objects.get(pk=student_id)
                Attendance.objects.create(student=student, date=date.today(), status=status)
        return redirect('attendance/success')

    students = Student.objects.all()
    return render(request, 'attendance.html', {'students': students})

def attendance_success(request):
    return HttpResponse("Attendance has been recorded successfully.")
