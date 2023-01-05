from django.db import models
from django.contrib.auth.models import AbstractUser,User,BaseUserManager, AbstractBaseUser,UserManager
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import make_password
from datetime import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import Group,Permission

class User(AbstractUser):
    class Meta:
        verbose_name = "Employers-User"

    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_perms')
    def __str__(self):
           return "Employer"

class UserProfile(models.Model):
    class Meta:
        verbose_name = "Employers-profile"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    company_name = models.CharField(max_length=255)
    def __str__(self):
           return self.user.username

class MyUser(AbstractUser):
    class Meta:
        verbose_name = "Candidates-Users"
    user_id = models.CharField(max_length=30,default='')
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, related_name='myuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='myuser_perms')
class Candidate(MyUser):
    pass

class CandidateProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

class Candidate_old(User):
    verbose_name = 'Candidate'
    User.username=models.CharField(max_length=100)
    User.email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    User.first_name = models.CharField(max_length=30)
    User.last_name = models.CharField(max_length=30)
    User.password = models.CharField(('password'), max_length=128)
    Id=models.CharField(max_length=9)
    USERNAME_FIELD = 'email'
    date_of_birth = models.DateField()
    phone_number = PhoneNumberField(blank=True)
    
    objects = UserManager()
        

from .choices import * 

class CVFormModel(models.Model):
    #user = models.OneToOneField(User)    
    field = models.IntegerField(choices=FIELD_CHOICES, default=1)   
    yearsexp = models.IntegerField(choices=YEARS_CHOICES, default=1)
    education = models.IntegerField(choices=EDUCATION_CHOICES, default=1)
    GitUrl = models.URLField(max_length=25)  
    file = models.FileField(upload_to='files/',default='files/default.pdf')

    def __str__(self):
           return self.GitUrl

