from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UserProfile
from django.utils import timezone
import uuid
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .utils import *

@login_required(login_url='/login/')
def indexView(request , **kwargs):
    context = get_context(request , **kwargs)
    return render(request, 'core/dashboard.html.j2', context)


def user_login(request):
    if request.method == 'POST':
        # Extract username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard page after login
        else:
            # Invalid credentials, render login page with error message
            return render(request, 'core/login.html.j2', {'error_message': 'Invalid username or password'})
    return render(request, 'core/login.html.j2')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def userprofile_list(request):
    userprofiles = UserProfile.objects.all()
    return render(request, 'userprofile/userprofile_list.html.j2', {'userprofiles': userprofiles})

def userprofile_detail(request, uniqueid):
    userprofile = get_object_or_404(UserProfile, uniqueid=uniqueid)
    return render(request, 'userprofile/userprofile_detail.html.j2', {'userprofile': userprofile})

def userprofile_create(request):
    if request.method == 'POST':
        # Extract form data from request
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        nick_name = request.POST.get('nick_name')
        father_name = request.POST.get('father_name')
        gender = request.POST.get('gender')
        birth_day = request.POST.get('birth_day')
        blood_group = request.POST.get('blood_group')
        pin = request.POST.get('pin')

        # Create UserProfile instance and save it
        UserProfile.objects.create(
            email=email,
            phone=phone,
            username=username,
            first_name=first_name,
            last_name=last_name,
            nick_name=nick_name,
            father_name=father_name,
            gender=gender,
            birth_day=birth_day,
            blood_group=blood_group,
            pin=pin,
            uniqueid=uuid.uuid4(),  # Generate unique UUID for primary key
            date_joined=timezone.now()
        )
        return redirect('userprofile-list')
    return render(request, 'userprofile/userprofile_form.html.j2')

def userprofile_update(request, uniqueid):
    userprofile = get_object_or_404(UserProfile, uniqueid=uniqueid)
    if request.method == 'POST':
        # Extract form data from request
        userprofile.email = request.POST.get('email')
        userprofile.phone = request.POST.get('phone')
        userprofile.username = request.POST.get('username')
        userprofile.first_name = request.POST.get('first_name')
        userprofile.last_name = request.POST.get('last_name')
        userprofile.nick_name = request.POST.get('nick_name')
        userprofile.father_name = request.POST.get('father_name')
        userprofile.gender = request.POST.get('gender')
        userprofile.birth_day = request.POST.get('birth_day')
        userprofile.blood_group = request.POST.get('blood_group')
        userprofile.pin = request.POST.get('pin')
        userprofile.save()
        return redirect('userprofile-detail', uniqueid=uniqueid)
    return render(request, 'userprofile/userprofile_form.html.j2', {'userprofile': userprofile})

def userprofile_delete(request, uniqueid):
    userprofile = get_object_or_404(UserProfile, uniqueid=uniqueid)
    if request.method == 'POST':
        userprofile.is_active = False
        return redirect('userprofile-list')
    return render(request, 'userprofile/userprofile_confirm_delete.html.j2', {'userprofile': userprofile})
