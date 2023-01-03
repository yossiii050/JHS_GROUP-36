from django import forms
from .models import Candidate,EmployerProfile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.models import User #impor user databased
from django.contrib.auth.models import Group
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CreateEmployerForm(UserCreationForm):
    CompanyName=forms.CharField(max_length=100)    
    is_active=False
    class Meta:
        captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
        model=User
        fields=['username','email','CompanyName','password1','password2','is_active']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
            group = Group.objects.get(name='Employers')
            user.groups.add(group)
        return user 
class CreateCandidateForm(UserCreationForm):
    class Meta:
        model=Candidate
        fields=('username','email','password1','password2','first_name','last_name','Id','date_of_birth') 
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            group = Group.objects.get(name='Candidate')
            user.groups.add(group)
        return user


class EmployerProfileForm(forms.ModelForm):
    
    class Meta:
        model = EmployerProfile
        fields = ['bio', 'avatar', 'contact_methods', 'location', ]

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    #contact_methods = forms.TextField()
    #location = forms.CharField(max_length=255)
    class Meta:
        model = EmployerProfile
        fields = ['bio', 'avatar' ]
from .choices import *
class CVForm(forms.Form):
    file      = forms.FileField() # for creating file input
    field = forms.ChoiceField(choices = FIELD_CHOICES, label="Field of work", initial='', widget=forms.Select(), required=True)
    yearsexp  = forms.ChoiceField(choices = YEARS_CHOICES,label="Years of experience",required=True)
    education = forms.ChoiceField(choices = EDUCATION_CHOICES, label="Education", widget=forms.Select(), required=True)
    GitUrl = forms.URLField(max_length=25,label= "Git-URL")     
