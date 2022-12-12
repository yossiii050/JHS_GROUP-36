from django import forms
from .models import Candidate

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.models import User #impor user databased


class CreateEmployerForm(UserCreationForm):
    age = forms.IntegerField()
    gender = forms.CharField()
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','age','gender','password1','password2']        
#
class CreateCandidateForm(forms.ModelForm):   
    class Meta:
        model=Candidate
        fields=('username','email','password','first_name','last_name')
    