from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Upload
from .forms import UploadForm
from django.views.generic import CreateView

def Upload_list(request):
    uploads=Upload.objects.all().order_by('date')
    return render(request,'jobs/Upload_list.html',{'uploads':uploads})

def uploadJob(request):
    submitted=False
    if request.method=="POST":
        form=UploadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/uploadJob?submittad=True')
    else:
        form=UploadForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'jobs/uploadJob.html',{'form':form,'submitted':submitted})
    #return HttpResponse('uploadJob')


def updateJob(request):
    return render(request,'jobs/updateJob.html')
    #return HttpResponse('updateJob')

def job_details(request,slug):
    job=Upload.objects.get(slug=slug)
    return render (request,'jobs/jobsDetails.html',{'job':job})

