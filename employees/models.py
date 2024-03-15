from django.db import models
from core.models import *

class Employee(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_employee")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, related_name="employee_department")
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True, blank=True, related_name="employee_designation")
    
    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"
