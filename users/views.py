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


# def candidateRegPage(request):
#     form = CreateCandidateForm()

#     if request.method == 'POST':
#         form = CreateCandidateForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('login')
        
#     context={'form':form}
#     return render(request, 'candidatereg.html',context)

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
            #return redirect('login')
    
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

from .models import CVForm
from .forms import CVForm  
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