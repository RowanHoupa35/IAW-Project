# signup/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, StudentProfile, TeacherProfile, StaffProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['Student_ID', 'School', 'Faculty', 'Department', 'Major', 'Level']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['School', 'Faculty', 'Department', 'Position', 'Grade']

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['Service', 'Position']
