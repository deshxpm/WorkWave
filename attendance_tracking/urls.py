from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_record_list, name='attendance_record_list'),
]