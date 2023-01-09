from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'body']
        exclude = ['date','user','handler','isopen','closed_by','Reply']
        
