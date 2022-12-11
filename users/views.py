from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from .forms import CreateEmployerForm,CreateCandidateForm

def employerRegPage(request):
    form=CreateEmployerForm()

    if request.method == 'POST':
        form=CreateEmployerForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'employerreg.html',context)

def candidateRegPage(request):
    form=CreateCandidateForm()

    if request.method == 'POST':
        form=CreateCandidateForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'candidatreg.html',context)