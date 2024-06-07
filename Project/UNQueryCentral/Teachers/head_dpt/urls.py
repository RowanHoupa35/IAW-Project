from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.head_dpt_dashboard, name='head_dpt_dashboard'),
    # Add more URLs specific to head of department here
]
