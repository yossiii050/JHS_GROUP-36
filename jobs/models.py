from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser,User,BaseUserManager, AbstractBaseUser
from decimal import Decimal
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .choices import * 
from decimal import *
from users.models import Employer



class Upload(models.Model): #The dataBase knows to create a table for this model
    title=models.CharField(max_length=60,null=True)
    #author=models.ForeignKey(User,on_delete=models.CASCADE)
    subTitle=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    body=models.TextField(max_length=200)
    date=models.DateTimeField(auto_now_add=True) #automaticly applied
    category = models.IntegerField(choices=FIELD_CHOICES, default=1)  
    salaryRange = models.IntegerField(choices=SALARY_CHOICES, default=1)   
    yearsexp = models.IntegerField(choices=YEARS_CHOICES, default=1)
    education=models.CharField(max_length=60,null=True)
    time=models.IntegerField(choices=TIME_CHOICES, default=1)
    hybrid=models.BooleanField(default=True)
    priority=models.IntegerField(choices=PRIORITY_CHOICES,default=1)
    owner=models.ForeignKey(Employer, on_delete=models.CASCADE, default=1, related_name='employer')
    location=models.IntegerField(choices=CITIES, default=1)
    availableAmount = models.DecimalField(max_digits=2, decimal_places=0, default=Decimal('5'))
    notification=models.DecimalField(max_digits=3 ,decimal_places=0, default=Decimal('5'))

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...' #take from 0 to 50 characters

    def get_absolute_url(self):
        return reverse("upload_detail", kwargs={"slug": self.slug})

