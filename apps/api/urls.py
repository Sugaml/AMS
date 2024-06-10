from django.urls import path
from . import api as views


urlpatterns = [
    path("", views.WelcomeView.as_view(), name="home_page"),
    path("login/", views.LoginView.as_view(), name="log_in_page"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path("home/", views.HomeView.as_view(), name="home_page"),
    path('add-student/', views.add_student_view, name='add-student'),
    path('add-student-success/', views.add_student_success, name='add-student-success'),
    path('attendance-report/', views.attendance_report_view, name='attendance-report'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('attendance-success/', views.attendance_success, name='attendance-success'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('students/', views.student_list_view, name='student-list'),

]