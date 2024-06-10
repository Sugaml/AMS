from django.views.generic import TemplateView
from decouple import config
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from apps.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .forms import StudentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.auth.views import LoginView, LogoutView
import csv
from django.core.paginator import Paginator
from django.db.models import Count, F





def dashboard_view(request):
    return render(request, 'apps/dashboard.html')

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "apps/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now()
        return context

    def get(self, request):
        user = request.user
        active_page="home"
        context = {
            "users": user,
            }
        return render(request, self.template_name, context)


class WelcomeView(TemplateView):
    template_name = "apps/welcome.html"

    def get(self, request):
        return render(request, self.template_name)
    
class LoginView(TemplateView):
    template_name = "apps/login.html"
    default_redirect = "/"

    # @method_decorator(login_required)
    def get(self, request):
        next = request.GET.get("next","/home/")
        return render(request, self.template_name)

    def post(self, request):
        next = request.POST.get("next","")
        if next == "/logout/":
            next = "/home/"
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        user = User.objects.filter(username=username).first()
        print(user)
        if user:
            if not user.is_active:
                messages.error(
                    request, "Login failed ! user is deactivated."
                )
                return HttpResponseRedirect(f"/login/?next={next}")

            user = authenticate(username=username, password=password)
            if user and user.is_authenticated:
                login(request, user)
                if next:
                    return HttpResponseRedirect(next)
                return redirect("home_page")

            messages.error(
                request, "Login failed ! password do not match."
            )
        else:
            messages.error(
                request, "Login failed ! username do not match."
            )
        return HttpResponseRedirect(f"/login/?next={next}")

def add_student_view(request):
    form = StudentForm()  # Ensure form is always initialized
    if request.method == 'POST':
        if 'form_submit' in request.POST:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add-student-success')
        elif 'csv_submit' in request.POST:
            csv_file = request.FILES.get('csv_file')
            if csv_file:
                handle_uploaded_csv(csv_file)
                return redirect('add-student-success')
    return render(request, 'apps/add_student.html', {'form': form})

def handle_uploaded_csv(csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)
    for row in reader:
        name, roll_number, course, dob, email = row
        # Check if a student with the same roll number and course already exists
        if not Student.objects.filter(roll_number=roll_number, course=course).exists():
            Student.objects.create(
                name=name,
                roll_number=roll_number,
                course=course,
                dob=dob,
                email=email
            )

def add_student_success(request):
    return render(request, 'apps/student_success.html')

def attendance_view(request):
    today = date.today()
    if Attendance.objects.filter(date=today).exists():
        return redirect('attendance-report')

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

def attendance_success(request):
    return render(request, 'apps/attendance_success.html')

def attendance_report_view(request):
    attendance_records = Attendance.objects.all().order_by('date', 'student')
    return render(request, 'apps/attendance_report.html', {'attendance_records': attendance_records})


def student_list_view(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        shift = request.POST.get('shift')
        students = Student.objects.filter(course=course)
        paginator = Paginator(students, 10)  # Show 10 students per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'apps/students.html', {'page_obj': page_obj, 'course': course, 'shift': shift})
    else:
        return render(request, 'apps/student_form.html')
    
def attendance_report(request):
    current_month = datetime.now().month
    current_year = datetime.now().year

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        attendance_data = Attendance.objects.filter(date__range=[start_date, end_date]).values('student__name').annotate(total_attendance=Count('id'), period=F('date'))
    else:
        attendance_data = Attendance.objects.filter(date__month=current_month, date__year=current_year).values('student__name').annotate(total_attendance=Count('id'), period=F('date'))

    return render(request, 'apps/attendance-month.html', {'attendance_data': attendance_data})