from django.shortcuts import render
from django.http import HttpResponse
from maintenance_mode.decorators import force_maintenance_mode_off, force_maintenance_mode_on
from maintenance_mode.core import get_maintenance_mode, set_maintenance_mode

set_maintenance_mode(True)

if get_maintenance_mode():
    set_maintenance_mode(False)

def index(request):
    return HttpResponse('Index page')


def maintenance(request):
    return render(request,'maintenance.html')

def maintenance(request):
    return render(request,'maintenance.html')    

def handler503(request):
    return render(request,"503.html",status=500)    