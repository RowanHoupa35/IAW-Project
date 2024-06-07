from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordResetView
from .forms import CustomAuthenticationForm, CustomPasswordResetForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_student:
                    return redirect('student_dashboard')  # Rediriger l'étudiant vers son interface
                elif user.is_teacher:
                    return redirect('teacher_dashboard')  # Rediriger l'enseignant vers son interface
                elif user.is_staff_member:
                    return redirect('staff_dashboard')  # Rediriger le personnel vers son interface
                else:
                    return redirect('default_dashboard')  # Rediriger les autres utilisateurs vers une interface par défaut
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login/login.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'login/password_reset.html'
    success_url = 'password_reset_done'


