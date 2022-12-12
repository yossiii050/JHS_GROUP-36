from django.db import models
from django.contrib.auth.models import AbstractUser,User,BaseUserManager, AbstractBaseUser
import os
from phonenumber_field.modelfields import PhoneNumberField

    
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    #password1 = models.CharField(max_length=50)
    #password2 = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    #website = models.URLField(blank=True)
    #date_of_birth = models.DateField()
    #phone_number = PhoneNumberField(blank=True)

    #is_active = models.BooleanField(default=True)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.name
