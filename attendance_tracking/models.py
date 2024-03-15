from django.db import models
from core.models import *

class AttendanceRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_attandance')
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')])

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.status}"
