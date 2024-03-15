from django.db import models
from core.models import *
from django.core.mail import send_mail

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status_choices = [
        ('Created', 'Created'),
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        ('Work in Progress', 'Work in Progress'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed'),
        ('Canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Created')
    assigned_to = models.ForeignKey(User, related_name='assigned_tickets', null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='created_tickets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def send_status_notification(self):
        subject = f"Ticket Status Update: {self.title}"
        message = f"Ticket status has been changed to '{self.status}'."
        send_mail(subject, message, 'from@example.com', [self.created_by.email])
