# teachers/dean/models.py

from django.db import models
from django.contrib.auth.models import User

class Query(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queries')
    department = models.CharField(max_length=255)
    query_type = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    attached_files = models.FileField(upload_to='attachments/', blank=True, null=True)

class Feedback(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='feedbacks')
    department_head = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
