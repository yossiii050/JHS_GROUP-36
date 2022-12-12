from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from .forms import CreateEmployerForm,CreateCandidateForm
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import get_object_or_404


def candidateRegPage(request):
    form = CreateCandidateForm()

    if request.method == 'POST':
        form = CreateCandidateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    context={'form':form}
    context['detail'] = CreateCandidateForm.objects.filter(id=1).name
    return render(request, 'candidatereg.html',context)


def employerRegPage(request):
    form=CreateEmployerForm()

    if request.method == 'POST':
        form=CreateEmployerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context={'form':form}
    return render(request,'employerreg.html',context)

# def candidateRegPage(request):
#     form=CreateCandidateForm()

#     if request.method == 'POST':
#         form = CreateCandidateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #return redirect('login')
    
#     context={'form':form}
#     return render(request,'candidatereg.html',context)

def loginPage(request):
    context={}
    return render(request,'login.html',context)
