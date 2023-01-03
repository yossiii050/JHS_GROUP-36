
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Ticket
from django.core.files import File
from .forms import TicketForm
from django.contrib import messages
from django.template import loader
<<<<<<< HEAD

from django.contrib.auth.models import Group
from django.http import FileResponse

from django.contrib.auth.models import Group,User




def ticket(request):    
    #tickets=ticket.objects
  return render(request,'ticket.html')#,{'tickets':tickets})
=======
from django.contrib.auth.models import Group
from django.http import FileResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.models import User


def create_ticket(request):
    if request.method == 'POST':
      form = TicketForm(request.POST)
      if form.is_valid():
            new_ticket = Ticket(
            title=form.cleaned_data['title'],body=form.cleaned_data['body'],user=request.user,handler=request.user)
            new_ticket.save()
            messages.success(request, 'Ticket saved successfully!')
            return render(request, 'tech.html', {'form': form, 'date':new_ticket.date})
    else:
        form = TicketForm()
    return render(request, 'ticket.html', {'form': form})
>>>>>>> e590062d5ed2e64d838c14de65861287b204cf23


def techhome(request):
    return render(request,'tech.html')

from sqlite3 import SQLITE_READ
def tech_main (request):
  return render(request,'tech_main.html')


def tech_approve_employer(request):
  form=User.objects.filter(is_active=False)
  #form=Group.name()
  context={'form':form}
  return render(request,'tech_approve_employer.html',context)

def update_status(request):
    if request.method == 'POST':
        User.objects.filter(is_active=False).update(is_active=True)
    return render(request,'tech.html')

#def tech_approve_employer1(request):
 # context = {} 
  #return render(request,'tech_approve_employer.html')