from django.shortcuts import render
from django.http import HttpResponse
from .models import Upload
from django.views.generic import DetailView

def Upload_list(request):
    uploads=Upload.objects.all().order_by('date')
    return render(request,'jobs/Upload_list.html',{'uploads':uploads})

def uploadJob(request):
    return render(request,'jobs/uploadJob.html')
    #return HttpResponse('uploadJob')

def upldateJob(request):
    return render(request,'jobs/updateJob.html')
    #return HttpResponse('updateJob')

def job_details(request,pk):
    return render (request,'jobs/jobsDetails.html')

#class job_details(DetailView):
 #   model=Upload
  #  template_name='jobsDetails.html'

# Create your views here.

