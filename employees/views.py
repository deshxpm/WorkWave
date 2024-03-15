from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Employee, LeaveRequest
from .serializers import EmployeeSerializer


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    leave_requests = LeaveRequest.objects.filter(employee=employee)
    return render(request, 'employee_detail.html', {'employee': employee, 'leave_requests': leave_requests})


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def leave_request_form(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave_request_form.html', {'form': form})
