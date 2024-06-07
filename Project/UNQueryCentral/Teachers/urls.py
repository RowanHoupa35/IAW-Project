# teachers/urls.py
from django.urls import path, include

urlpatterns = [
    path('dean/', include('Teachers.dean.urls')),
    path('head_dpt/', include('Teachers.head_dpt.urls')),
]
