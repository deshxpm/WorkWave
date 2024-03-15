from django.shortcuts import render
from .models import PerformanceReview

def performance_review_list(request):
    performance_reviews = PerformanceReview.objects.all()
    return render(request, 'performance_review_list.html', {'performance_reviews': performance_reviews})
