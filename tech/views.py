
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import ticket
from django.core.files import File
from django.template import loader
from django.contrib.auth.models import Group




def ticket(request):
    
    #tickets=ticket.objects
    return render(request,'ticket.html')#,{'tickets':tickets})


def techhome(request):
    return render(request,'tech.html')

from sqlite3 import SQLITE_READ
def tech_main (request):
  return render(request,'tech_main.html')


def tech_approve_employer(request):
 # my_group=Group.objects.get(name="pending")
  form=Group.name()
  context={'form':form}
  return render(request,'tech_approve_employer.html',context)


#def tech_approve_employer1(request):
 # context = {} 
  #return render(request,'tech_approve_employer.html')