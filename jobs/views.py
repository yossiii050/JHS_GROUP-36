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

def job_details(request,slug):
    job=Upload.objects.get(slug=slug)
    return render (request,'jobs/jobsDetails.html',{'job':job})

#class job_details(DetailView):
 #   model=Upload
  #  template_name='jobsDetails.html'

# Create your views here.
from .functions import handle_uploaded_file
from .models import StudentForm
from .forms import StudentForm  
def index(request):  
    if request.method == 'POST':  
        
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"cv.html",{'form':student})