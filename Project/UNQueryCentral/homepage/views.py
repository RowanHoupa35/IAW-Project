# homepage/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'homepage/home.html')
