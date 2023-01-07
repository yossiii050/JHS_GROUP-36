
from .choices import * 
from django.db import models
class CVFormModel(models.Model):
    #user = models.OneToOneField(User)    
    field = models.IntegerField(choices=FIELD_CHOICES, default=1)   
    yearsexp = models.IntegerField(choices=YEARS_CHOICES, default=1)
    education = models.IntegerField(choices=EDUCATION_CHOICES, default=1)
    GitUrl = models.URLField(max_length=25)  
    file = models.FileField(upload_to='files/',default='files/default.pdf')

    def __str__(self):
           return self.GitUrl

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=255)
    employer_id = models.CharField(max_length=200,unique=True)
    is_employer = models.BooleanField(default=True)
    bios=models.TextField(blank=True,default="write you bio here...")
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    USERNAME_FIELD='username'

    def __str__(self):
        return self.user.username

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=50)
    candidate_id = models.CharField(max_length=200,unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=255)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    is_candidate = models.BooleanField(default=True)
    bios=models.TextField(blank=True,default="write you bio here...")
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    USERNAME_FIELD='username'
    
    def __str__(self):
        return self.user.username
        

    def _str_(self):
        return self.user.username