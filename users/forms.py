from django import forms
from .models import Candidate
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.models import User #impor user databased
from django.contrib.auth.models import Group
#User=get_user_model()

class UserUpdateForm(forms.ModelForm):
    description=forms.CharField(max_length=100)
    bio=forms.CharField(max_length=500) 

    class Meta:
        model = User
        fields = ['bio','description']

class CreateEmployerForm(UserCreationForm):
    CompanyName=forms.CharField(max_length=100)    
    is_active=False
    description=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['username','email','password1','password2','CompanyName','description','is_active']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
            group = Group.objects.get(name='Employers')
            user.groups.add(group)
        return user            
#
class CreateCandidateForm(UserCreationForm):
    class Meta:
        model=Candidate
        fields=('username','email','password1','password2','first_name','last_name','Id','date_of_birth','phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            group = Group.objects.get(name='Candidate')
            user.groups.add(group)
        return user


from .choices import *
class CVForm(forms.Form):
    file      = forms.FileField() # for creating file input
    field = forms.ChoiceField(choices = FIELD_CHOICES, label="Field of work", initial='', widget=forms.Select(), required=True)
    yearsexp  = forms.ChoiceField(choices = YEARS_CHOICES,label="Years of experience",required=True)
    education = forms.ChoiceField(choices = EDUCATION_CHOICES, label="Education", widget=forms.Select(), required=True)
    GitUrl = forms.URLField(max_length=25,label= "Git-URL")     
