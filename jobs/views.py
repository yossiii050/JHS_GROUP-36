from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Upload
from .forms import UploadForm
from django.views.generic import CreateView

def Upload_list(request):
    uploads=Upload.objects.all().order_by('?')
    return render(request,'jobs/Upload_list.html',{'uploads':uploads})

def uploadJob(request):
    submitted=False
    if request.method=="POST":
        form=UploadForm(request.POST)
        if form.is_valid():
            form.instance.slug = form.cleaned_data['title']
            #form.instance.owner_id = request.user.id  # set the owner_id field to the id of the currently 
            form.save()
            submitted=True
            return render(request,'jobs/success.html')
    else:
        form=UploadForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'jobs/uploadJob.html',{'form':form,'submitted':submitted})
    #return HttpResponse('uploadJob')


def updateJob(request,upload_id):
    job=Upload.objects.get(slug=upload_id)
    form=UploadForm(request.POST or None,instance=job)
    if form.is_valid():
        form.instance.slug = form.cleaned_data['title']
        form.save()
        return render(request,'jobs/success.html')
    return render(request,'jobs/updateJob.html',{'job':job,'form':form})
    #return HttpResponse('updateJob')

def job_details(request,slug):
    job=Upload.objects.get(slug=slug)
    #job=Upload.objects.filter(slug=slug.values())
    return render (request,'jobs/jobsDetails.html',{'job':job})

def success(request):
    return render(request,'jobs/success.html')

def deleteJob(request,upload_id):
    job=Upload.objects.get(slug=upload_id)
    job.delete()
    return render(request,'jobs/success.html',{'job':job})
