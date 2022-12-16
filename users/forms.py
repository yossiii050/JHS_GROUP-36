from django import forms
from .models import Candidate

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.models import User #impor user databased


class CreateEmployerForm(UserCreationForm):
    age = forms.IntegerField()
    gender = forms.CharField()
    is_active=False
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','age','gender','password1','password2','is_active']        
#
class CreateCandidateForm(UserCreationForm):
    class Meta:
        model=Candidate
        fields=('username','email','password1','password2','first_name','last_name','Id','date_of_birth','phone_number')        #verbose_name = 'Candidate'
        #verbose_name_plural = 'Candidates''password1','password2'
    