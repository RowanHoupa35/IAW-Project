# signup/views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, StudentProfileForm, TeacherProfileForm, StaffProfileForm
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = None
        
        if 'category' in request.POST:
            category = request.POST['category']
            if category == 'student':
                profile_form = StudentProfileForm(request.POST)
            elif category == 'teacher':
                profile_form = TeacherProfileForm(request.POST)
            elif category == 'staff':
                profile_form = StaffProfileForm(request.POST)
            
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('login')
    else:
        user_form = CustomUserCreationForm()
        profile_form = None
    
    return render(request, 'signup/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
