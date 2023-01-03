from django import forms
from .models import Candidate,CVFormModel,UserProfile,CandidateProfile
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.models import User #impor user databased
from django.contrib.auth.models import Group
#User=get_user_model()

class UserUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    company_name = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = User
        fields = ['bio','company_name']

class CreateEmployerForm(UserCreationForm):
    is_active=False
    CompanyName=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['username','email','password1','password2','CompanyName','is_active']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.description="test"
        if commit:
            user.save()
            group = Group.objects.get(name='Employers')
            user.groups.add(group)
        return user            
#

""" class CreateEmployerForm_old(UserCreationForm):
    #CompanyName=forms.CharField(max_length=100)    
    is_active=False
    description=forms.CharField(max_length=100)
    class Meta:
        model=UserProfile
        fields=['username','email','password1','password2','CompanyName','description','is_active']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.description="test"
        if commit:
            user.save()
            group = Group.objects.get(name='Employers')
            user.groups.add(group)
        return user  """           
#
class CreateCandidateForm(UserCreationForm, ModelForm):
    class Meta:
        model = Candidate
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name','Id','date_of_birth','phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            group = Group.objects.get(name='Candidate')
            user.groups.add(group)
        return user

class CandidateProfileForm(ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = CandidateProfile
        fields = ['bio']



# class CreateCandidateForm_old(UserCreationForm):
#     class Meta:
#         model=Candidate
#         fields=('username','email','password1','password2','first_name','last_name','Id','date_of_birth','phone_number')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#             group = Group.objects.get(name='Candidate')
#             user.groups.add(group)
#         return user


from .choices import *
class CVForm(forms.Form):
    #file      = forms.FileField() # for creating file input    
    field = forms.ChoiceField(choices = FIELD_CHOICES, label="Field of work", initial='', widget=forms.Select(), required=True)
    yearsexp  = forms.ChoiceField(choices = YEARS_CHOICES,label="Years of experience",required=True)
    education = forms.ChoiceField(choices = EDUCATION_CHOICES, label="Education", widget=forms.Select(), required=True)
    GitUrl = forms.URLField(max_length=25,label= "Git-URL")  
    class Meta:
       model = CVFormModel
       fields = ['field', 'yearsexp', 'education', 'GitUrl']        
