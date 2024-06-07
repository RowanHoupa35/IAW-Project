# urls.py

from django.urls import path
from .views import login_view, CustomPasswordResetView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login/', CustomPasswordResetView.as_view(), name='password_reset'),
]
