from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from .choices import *
from django.conf import settings
User = settings.AUTH_USER_MODEL
import uuid

def validate_file_size(value):
    from django.core.exceptions import ValidationError
    filesize= value.size
    
    if filesize > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Country(Base):
    name      = models.CharField(max_length=100)
    sort_name = models.CharField(max_length=30)
    code      = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name        

class State(Base):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="state_country")

    def __str__(self):
        return self.name

class District(Base):
    name = models.CharField(max_length=150)
    district_state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="district_state")

    def __str__(self):
        return self.name

class City(Base):
    name = models.CharField(max_length=150)
    city_district = models.ForeignKey(District , on_delete=models.PROTECT , related_name="city_district",null=True)

    def __str__(self):
        return self.name
    
class Address(Base):
    address = models.TextField(max_length=500,null=True,blank=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, related_name="address_country")
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=True, related_name="address_state")
    district = models.ForeignKey('District', on_delete=models.CASCADE, null=True, related_name="address_district")
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True, related_name="address_city")
    pincode = models.CharField(max_length=20, null=True, blank=True)
    address_type = models.CharField(choices=ADDRESS_TYPE, max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.address}'

class UnitType(Base):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class HsnCode(Base):
    name = models.CharField(max_length=200)
    gst_percentage = models.DecimalField(max_digits=50, decimal_places=2, null=True,blank=True)

    def __str__(self):
        return f"{self.name}"

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, username, phone, password, **extra_fields)

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True) #HR administrators, managers, employees
    permissions = models.ManyToManyField('Permission', blank=True)

    def __str__(self):
        return self.name
    
class Permission(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone = models.CharField(max_length=20, default=None, null=True, unique=True)
    username = models.CharField(max_length=30, unique=True)# Keep the username field
    date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom fields
    uniqueid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    nick_name = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to="profile_picture/", blank=True, null=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, related_name="profile_company")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Other')
    birth_day = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default=None, null=True)
    is_verified = models.BooleanField(default=False)
    mobile_otp = models.CharField(max_length=10, null=True, blank=True)
    email_otp = models.CharField(max_length=10, null=True, blank=True)
    pin = models.CharField(max_length=4, null=True, blank=True)
    roles = models.ManyToManyField(Role, blank=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'phone'  # Set phone as the USERNAME_FIELD
    REQUIRED_FIELDS = ['username', 'email']  # Require username and email during user creation

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None): #This method checks whether the user has a specific permission (perm) on an object (obj). It returns True if the user has the permission, and False otherwise.
        # Adjust this method to check user permissions based on roles
        return self.is_superuser

    def has_module_perms(self, app_label): #This method checks whether the user has any permissions for a given application label (app_label). It returns True if the user has permissions for the app, and False otherwise.
        # Adjust this method to check user permissions based on roles
        return self.is_superuser

    def get_role_permissions(self):
        permissions = set()
        for role in self.roles.all():
            permissions.update(role.permissions.all())
        return permissions


class Company(Base):
    user    = models.ForeignKey('UserProfile', on_delete=models.CASCADE,related_name="company_user")
    uniqueid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email   = models.EmailField(verbose_name="email", max_length=60,null=True, blank=True)
    phone   = models.CharField(max_length=20,blank=True,null=True)
    gst_no  = models.CharField(max_length=50,null=True,blank=True)
    name    = models.CharField(max_length=200,unique=True)
    sort_name=models.CharField(max_length=50,null=True,blank=True)
    companytype = models.CharField(max_length=50,blank=True,null=True)
    logo    = models.FileField(upload_to="company_logo/",blank=True,null=True, validators=[validate_file_size])
    watermark = models.FileField(upload_to='company_watermark',blank=True, null=True, validators=[validate_file_size])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['uniqueid']),
            models.Index(fields=['name']),
            models.Index(fields=['gst_no']),
            models.Index(fields=['phone']),
            models.Index(fields=['is_active']),
        ]
            

class Department(Base):
    company = models.ForeignKey('UserProfile', on_delete=models.CASCADE,related_name="department_company")
    name    = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.name}"

class Designation(Base):
    company = models.ForeignKey('UserProfile', on_delete=models.CASCADE,related_name="designation_company")
    name    = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.name}"
