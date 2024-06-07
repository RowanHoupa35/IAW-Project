from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Request, Feedback, Teacher

@login_required
def dean_home(request):
    latest_requests = Request.objects.order_by('-created_at')[:10]
    return render(request, 'dean/home.html', {'requests': latest_requests})

@login_required
def dean_dashboard(request):
    # Logic to fetch and prepare data for charts
    return render(request, 'dean/dash.html')

@login_required
def dean_feedbacks(request):
    feedbacks = Feedback.objects.filter(teacher__user=request.user)
    return render(request, 'dean/feedbacks.html', {'feedbacks': feedbacks})

@login_required
def dean_history(request):
    requests = Request.objects.all()
    return render(request, 'dean/history.html', {'requests': requests})

@login_required
def dean_settings(request):
    # Logic to handle settings update
    return render(request, 'dean/settings.html')

@login_required
def request_detail(request, request_id):
    req = get_object_or_404(Request, pk=request_id)
    return render(request, 'dean/query_details.html', {'request': req})
