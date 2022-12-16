
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import ticket
from django.core.files import File


def ticket(request):
    
    #tickets=ticket.objects
    return render(request,'ticket.html')#,{'tickets':tickets})


def techhome(request):
    return render(request,'tech.html')


