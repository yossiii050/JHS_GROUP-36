from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from .forms import CreateEmployerForm,CreateCandidateForm
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import  redirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from .functions import handle_uploaded_file  

from django.contrib.auth.hashers import make_password

def changestatus(request):
    user = User.objects.get()
    user.is_active = True
    user.save()

def approveEmp(request):
    form=User.objects.filter(is_active=False)
    context={'form':form}
    return render(request,'appr.html',context)

def ReportEmployer(request):
    form=User.objects.all()
    context={'form':form}
    return render(request,'reportEmployer.html',context)

def ReportCandidate(request):
    form=Candidate.objects.all()
    context={'form':form}
    return render(request,'reportCandidate.html',context)

def employerRegPage(request):
    form=CreateEmployerForm()

    if request.method == 'POST':
        form=CreateEmployerForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')

    context={'form':form}
    return render(request,'employerreg.html',context)


def candidateRegPage(request):
    form=CreateCandidateForm()

    if request.method == 'POST':
        form = CreateCandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context={'form':form}
    return render(request,'candidatereg.html',context)

def loginPage(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if(user is not None):
            login(request,user)
            return redirect('home page')
        else:
            messages.info(request,'Username OR Password is incorrect')
            
    context={}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

from users.models import CVForm
from users.forms import CVForm  
def index(request):  
    if request.method == 'POST':  
        
        student = CVForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly",usershome)  
    else:  
        student = CVForm()  
        return render(request,"cv.html",{'form':student})  

def usershome(request):
    return render(request,'users.html')

from users.reports import registered_users_report

def registered_users(request):
    # Generate the report data
    data = registered_users_report()

    # Render the template with the report data
    return render(request, 'reports.html', data)