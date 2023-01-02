
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import ticket
from django.core.files import File
from .forms import TicketForm

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            new_ticket = ticket(title=form.cleaned_data['title'], body=form.cleaned_data['body'])
           # new_ticket = ticket(title='My ticket', body='This is the body of my ticket')
            new_ticket.save()
            #return redirect('tech', pk=new_ticket.pk)
            return render(request,'tech.html')

    else:
        form = TicketForm()
    return render(request, 'ticket.html', {'form': form})


def techhome(request):
    return render(request,'tech.html')


