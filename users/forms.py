from django import forms
from users import models

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.models import User #impor user databased


class CreateEmployerForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']        

class CreateCandidateForm(UserCreationForm):   
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']