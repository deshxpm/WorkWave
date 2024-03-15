from django.urls import path
from .views import performance_review_list
urlpatterns = [
    path('', performance_review_list, name='performance_review_list'),
]

