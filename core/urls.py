from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name="dashboard"),
    path('userprofiles/', views.userprofile_list, name='userprofile-list'),
    path('userprofile-detail/<uuid:uniqueid>/', views.userprofile_detail, name='userprofile-detail'),
    path('userprofiles/register/', views.userprofile_create, name='userprofile-create'),
    path('userprofiles/<uuid:uniqueid>/update/', views.userprofile_update, name='userprofile-update'),
    path('userprofiles/<uuid:uniqueid>/delete/', views.userprofile_delete, name='userprofile-delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('otp-verification/', views.otp_verification, name='otp_verification'),
]
