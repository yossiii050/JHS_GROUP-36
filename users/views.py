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
from django.contrib.auth.hashers import make_password

def stud(request):
    form=User.objects.all()
    context={'form':form}
    return render(request,'v.html',context)

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
            password = make_password(form['password1'])
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