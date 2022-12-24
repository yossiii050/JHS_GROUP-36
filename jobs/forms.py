
from django import forms
from django.forms import ModelForm #add data to database
from .models import Upload

from .choices import *
from . import models
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.models import User #impor user databased
from .choices import * 

class UploadForm(ModelForm):
    class Meta:
        model=Upload
        fields=('title','body','category','salaryRange','yearsexp','education','time','hybrid')
        # labels={ 'title':forms.TextInput(attrs={'class':'form-control'}),
        # 'body':forms.TextInput(attrs={'class':'form-control'}),
        # 'category':forms.TextInput(attrs={'class':'form-control'}),
        # 'salaryRange':forms.TextInput(attrs={'class':'form-control'}),
        # 'yearsexp':forms.TextInput(attrs={'class':'form-control'}),
        # 'education':forms.TextInput(attrs={'class':'form-control'}),
        # 'time':forms.TextInput(attrs={'class':'form-control'}),
        # 'hybrid':forms.TextInput(attrs={'class':'form-control'})}
        # widgets={
        # 'title':forms.TextInput(attrs={'class':'form-control'}),
        # 'body':forms.TextInput(attrs={'class':'form-control'}),
        # 'category':forms.TextInput(attrs={'class':'form-control'}),
        # 'salaryRange':forms.TextInput(attrs={'class':'form-control'}),
        # 'yearsexp':forms.TextInput(attrs={'class':'form-control'}),
        # 'education':forms.TextInput(attrs={'class':'form-control'}),
        # 'time':forms.TextInput(attrs={'class':'form-control'}),
        # 'hybrid':forms.TextInput(attrs={'class':'form-control'})
        # }


# class Upload(forms.Form):
#     title=models.CharField(max_length=60,null=True)
#     #author=models.ForeignKey(User,on_delete=models.CASCADE)
#     subTitle=models.Charfield(max_length=100)
#     slug=models.SlugField()
#     body=models.TextField(max_length=200)
#     date=models.DateTimeField(auto_now_add=True) #automaticly applied
#     category = models.IntegerField(choices=FIELD_CHOICES, default=1)  
#     salaryRange = models.IntegerField(choices=SALARY_CHOICES, default=1)   
#     yearsexp = models.IntegerField(choices=YEARS_CHOICES, default=1)
#     education=models.CharField(max_length=60,null=True)
#     time=models.IntegerField(choices=TIME_CHOICES, default=1)
#     hybrid=models.BooleanField(default=True)
