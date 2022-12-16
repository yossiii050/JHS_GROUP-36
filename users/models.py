from django.db import models
from django.contrib.auth.models import AbstractUser,User,BaseUserManager, AbstractBaseUser,UserManager
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import make_password

    
class Candidate(AbstractBaseUser):
    verbose_name = 'Candidate'

    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #name = models.CharField(max_length=128)
    #User.username=models.CharField(max_length=100)
    USERNAME_FIELD = 'username'
    username=models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    #is_active = models.BooleanField()#default=False)
    #User.first_name = models.CharField(max_length=30)
    #User.last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=150)

    #UserCreationForm.password1=models.CharField(max_length=50)
    #UserCreationForm.password2=models.CharField(max_length=50)
    #website = models.URLField(blank=True)
    #date_of_birth = models.DateField()
    #phone_number = PhoneNumberField(blank=True)

    
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']

    