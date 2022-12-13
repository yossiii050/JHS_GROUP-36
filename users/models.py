from django.db import models
from django.contrib.auth.models import AbstractUser,User,BaseUserManager, AbstractBaseUser
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

    
class Candidate(User):
    verbose_name = 'Candidate'

    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #name = models.CharField(max_length=128)
    User.username=models.CharField(max_length=100)
    #username = models.CharField(max_length=100)
    User.email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    #User.password1 = models.CharField(max_length=50)
    #User.password2 = models.CharField(max_length=50)
    User.first_name = models.CharField(max_length=30)
    User.last_name = models.CharField(max_length=30)
    User.password = models.CharField(max_length=50)
    #password1=User.set_password(max_length=50)
    #UserCreationForm.password1=models.CharField(max_length=50)
    #UserCreationForm.password2=models.CharField(max_length=50)
    #website = models.URLField(blank=True)
    #date_of_birth = models.DateField()
    #phone_number = PhoneNumberField(blank=True)

    #is_active = models.BooleanField(default=True)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']

    
       

