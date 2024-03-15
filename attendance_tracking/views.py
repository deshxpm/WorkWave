from django.shortcuts import render
from .models import AttendanceRecord

def attendance_record_list(request):
    attendance_records = AttendanceRecord.objects.all()
    return render(request, 'attendance_record_list.html', {'attendance_records': attendance_records})