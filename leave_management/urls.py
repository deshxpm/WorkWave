from django.urls import path
from . import views

urlpatterns = [
    path('', views.leave_request_list, name='leave_request_list'),
]