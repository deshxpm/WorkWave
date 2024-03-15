from django.db import models
from core.models import *

class LeaveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_request_user')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"Leave Request by {self.user.username}"
