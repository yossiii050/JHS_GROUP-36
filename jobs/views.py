from django.shortcuts import render
from django.http import HttpResponse
from .models import Upload


def Upload_list(request):
    uploads=Upload.objects.all().order_by('date')
    return render(request,'jobs/Upload_list.html',{'uploads':uploads})

def uploadJob(request):
    return render(request,'jobs/uploadJob.html')
    #return HttpResponse('uploadJob')

def upldateJob(request):
    return render(request,'jobs/updateJob.html')
    #return HttpResponse('updateJob')

def job_details(request,slug):
    return HttpResponse(slug)

# Create your views here.
