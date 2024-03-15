from django.urls import path
from .views import employee_list, employee_detail, EmployeeListCreateAPIView, EmployeeDetailAPIView 

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('<int:employee_id>/', employee_detail, name='employee_detail'),
    # path('leave-request/', leave_request_form, name='leave_request_form'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
]