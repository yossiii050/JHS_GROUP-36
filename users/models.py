from django.db import models
from django.contrib.auth.models import AbstractUser,User,BaseUserManager, AbstractBaseUser,UserManager
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import make_password
from datetime import timezone

class Candidate(User):
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
        



    