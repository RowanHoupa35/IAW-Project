# teachers/dean/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dean_home, name='dean_home'),
    path('dashboard/', views.dean_dashboard, name='dean_dashboard'),
    path('feedbacks/', views.dean_feedbacks, name='dean_feedbacks'),
    path('history/', views.dean_history, name='dean_history'),
    path('settings/', views.dean_settings, name='dean_settings'),
    path('query/<int:query_id>/', views.query_detail, name='query_detail'),
]
