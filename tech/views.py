from django.http import HttpResponse
from django.shortcuts import render
def reg22(request):
    return HttpResponse("This is a register page.")

def ticket(request):
    return render(request,'ticket.html')

