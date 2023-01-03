
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import ticket
from django.core.files import File
from django.template import loader

from django.contrib.auth.models import Group
from django.http import FileResponse

from django.contrib.auth.models import Group,User




def ticket(request):    
    #tickets=ticket.objects
  return render(request,'ticket.html')#,{'tickets':tickets})


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