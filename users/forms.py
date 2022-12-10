from django import forms
from users import models
class UserForm(forms.ModelForm):
    class Meta:
        model = models.Candidate
        widgets = {
            'password': forms.PasswordInput(),
        }
        