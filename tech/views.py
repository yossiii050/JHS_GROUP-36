
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Ticket
from django.core.files import File
from .forms import TicketForm
from django.contrib import messages

def create_ticket(request):
    if request.method == 'POST':
      form = TicketForm(request.POST)
      if form.is_valid():
            new_ticket = Ticket(
            title=form.cleaned_data['title'],body=form.cleaned_data['body'])
            new_ticket.save()
            messages.success(request, 'Ticket saved successfully!')
            return redirect('home')

    else:
        form = TicketForm()
    return render(request, 'ticket.html', {'form': form})


def techhome(request):
    return render(request,'tech.html')


