from django.http import HttpResponse
from django.shortcuts import render,redirect

def home_page_view(request,*args, **kwargs):
    return render(request,"home.html",{})

#def home_template(request):
 #   context={}
  #  return render(request,'home.html',context)