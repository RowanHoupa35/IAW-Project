# signup/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    is_dean = models.BooleanField(default=False)
    is_department_head = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser_permissions',
    )

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,)
    Student_ID = models.CharField(max_length=100,primary_key=True)
    School = models.CharField(max_length=100)
    Faculty = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Major = models.CharField(max_length=100)
    Level = models.CharField(max_length=50)

class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    School = models.CharField(max_length=100)
    Faculty = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Grade = models.CharField(max_length=50)

class StaffProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    Service = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
