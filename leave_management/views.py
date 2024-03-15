from django.shortcuts import render
from .models import LeaveRequest

def leave_request_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leave_request_list.html', {'leave_requests': leave_requests})
