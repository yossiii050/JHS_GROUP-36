from django import forms
from .models import CVFormMode,CVFormModell
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Employer, Candidate,EmployerProfile,CandidateProfile
from django.contrib.auth.hashers import make_password

class EmployerSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Employer
        fields = ['username', 'email', 'password1', 'password2', 'CompanyName', 'employer_id','is_employer','bios']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(EmployerSignUpForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class CandidateSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Candidate
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'candidate_id', 'date_of_birth', 'phone_number','bios']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(CandidateSignUpForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name','date_of_birth', 'phone_number','bios']

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['CompanyName', 'employer_id','bios']

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['candidate_bio']

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['employer_bio']

class CandidateEditProfileForm(CandidateForm, CandidateProfileForm):
    pass

class EmployerEditProfileForm(EmployerForm, EmployerProfileForm):
    pass



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
