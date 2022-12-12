
from django.shortcuts import render
from .models import ticket

def ticket(request):
    tickets=ticket.objects
    return render(request,'tech/ticket.html',{'tickets':tickets})

