from django.db import models
from django.contrib.auth.models import User

class Faculty(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_dean = models.BooleanField(default=False)
    is_head_dpt = models.BooleanField(default=False)
    grade = models.CharField(max_length=100)

class Request(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    attached_files = models.FileField(upload_to='requests/', null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    feedback_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
