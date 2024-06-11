from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class CustomUser(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField(default=timezone.now)
    email = models.EmailField(default='example@example.com')
    mobile_num = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    shift = models.CharField(max_length=100,default='morning')
    dob = models.DateField(default=timezone.now)
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
