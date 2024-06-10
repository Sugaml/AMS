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
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-student-success')
    else:
        form = StudentForm()
    return render(request, 'apps/add_student.html', {'form': form})


def add_student_success(request):
    return HttpResponse("Student has been added successfully.")

def attendance_view(request):
    if request.method == 'POST':
        for student_id, status in request.POST.items():
            if student_id.startswith('student_'):
                student_id = student_id.split('_')[1]
                student = Student.objects.get(pk=student_id)
                Attendance.objects.create(student=student, date=date.today(), status=status)
        return redirect('attendance-success')

    students = Student.objects.all()
    return render(request, 'apps/attendance.html', {'students': students})

def attendance_success(request):
    return render(request, 'apps/attendance_success.html')

def attendance_report_view(request):
    attendance_records = Attendance.objects.all().order_by('date', 'student')
    return render(request, 'apps/attendance_report.html', {'attendance_records': attendance_records})