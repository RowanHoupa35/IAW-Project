# teachers/dean/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from Teachers.models import Feedback
from .models import Query

@login_required
def dean_home(request):
    # Fetch the 10 most recent queries
    recent_queries = Query.objects.order_by('-created_at')[:10]
    context = {'recent_queries': recent_queries}
    return render(request, 'teachers/dean/dean_home.html', context)

@login_required
def dean_dashboard(request):
    # Logic to display the dashboard with charts
    # This could include aggregating query data by department, type, etc.
    # Here we just pass an empty context for simplicity
    context = {}
    return render(request, 'teachers/dean/dean_dashboard.html', context)

@login_required
def dean_feedbacks(request):
    # Fetch feedbacks from department heads
    # Assuming there is a Feedback model linked to queries
    feedbacks = Feedback.objects.all()  # Replace with actual filtering logic
    context = {'feedbacks': feedbacks}
    return render(request, 'teachers/dean/dean_feedbacks.html', context)

@login_required
def dean_history(request):
    # Fetch the full history of queries
    queries = Query.objects.all()
    context = {'queries': queries}
    return render(request, 'teachers/dean/dean_history.html', context)

@login_required
def dean_settings(request):
    # Logic to handle settings update
    if request.method == 'POST':
        # Handle the form submission here
        # For example, updating the user's profile information
        pass
    return render(request, 'teachers/dean/dean_settings.html')

@login_required
def query_detail(request, query_id):
    # Fetch the specific query by its ID
    query = get_object_or_404(Query, id=query_id)
    context = {'query': query}
    return render(request, 'teachers/dean/query_detail.html', context)
