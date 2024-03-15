from django.shortcuts import render
from .models import HRMetric

def hr_metrics_dashboard(request):
    hr_metrics = HRMetric.objects.all()
    return render(request, 'hr_metrics_dashboard.html', {'hr_metrics': hr_metrics})
