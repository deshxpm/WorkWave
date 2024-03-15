from django.shortcuts import render
from .models import Notification

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notification_list.html', {'notifications': notifications})
