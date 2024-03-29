
from django import forms
from django.forms import ModelForm #add data to database
from .models import Upload

from .choices import *
from . import models
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from django.contrib.auth.models import User #impor user databased
from .choices import * 
from django import forms
class UploadForm(ModelForm):
    class Meta:
        model=Upload
        fields=('title','subTitle','body','category','salaryRange','yearsexp','education','time','hybrid','priority','location','availableAmount','notification','owner')
        exclude =['owner','notification_count']
        
class SortForm(forms.Form):
    SORT_FIELD_CHOICES = (("title", "Title"), ("date", "Date"),("salaryRange","Salary Range"),("yearsexp","Years of expirience"),("time","Job Type"),("hybrid","Hybrid"),("location","Location"),("viewsCounter","Views"))  # Add more choices here to support additional sort fields
    SORT_ORDER_CHOICES = (("ascending", "Ascending"), ("descending", "Descending"))

    sort_field = forms.ChoiceField(
        choices=SORT_FIELD_CHOICES,  # Set the choices for this field
        required=True,  # This field is required (cannot be left blank)
    )
    sort_order = forms.ChoiceField(
        choices=SORT_ORDER_CHOICES,  # Set the choices for this field
        required=True,  # This field is required (cannot be left blank)
    )


