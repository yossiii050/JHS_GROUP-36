from django.db import models
from django.contrib.auth.models import User,BaseUserManager, AbstractBaseUser
import os

class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    #date_of_birth = models.DateField()

    #is_active = models.BooleanField(default=True)

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.name
