from django import forms
from .models import ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['title', 'body']