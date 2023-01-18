from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from .models import Upload
from .forms import UploadForm,SortForm
from django.views.generic import CreateView
from django.db.models.functions import Lower
import csv
import json
from django.http import FileResponse
import io
from django.urls import reverse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
#from .forms import JobApplicationForm
from django.contrib.auth.models import User
from users.models import Candidate,Employer
from django.shortcuts import HttpResponseRedirect

def jobsPriorityPdfFile(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
   
    #c.saveState()
    #c.rotate(180)
    #c.drawImage(image, x=10, y=10, width=100, height=100)
    #c.restoreState()

    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica-Bold",10)
    
    image_path = 'C:\JHS_GROUP-36\static\jpg\LOGO.jpg'
    image = ImageReader(image_path)
    c.drawImage(image, x=200, y=-50, width=250, height=200)
    

    jobs=Upload.objects.filter(priority=1)
    lines=[" "," "," "," "," "," "," "]
    textob.setFont("Helvetica-Bold", 15)
    lines.append("High-Priority Jobs Report")

    for job in jobs:
        lines.append("                                 ")
        textob.setFont("Helvetica-Bold", 12)
        lines.append('Job Title: '+job.title)
        textob.setFont("Helvetica-Bold", 10)
        lines.append('Sub Title: '+job.subTitle)
        textob.setFont("Helvetica", 10)
        lines.append(job.body)
        lines.append('Date of Publish: '+str(job.date))
        category = job.get_category_display()
        lines.append('Category: '+category)
        salaryRange = job.get_salaryRange_display()
        lines.append('Salary Range: '+salaryRange)
        yearsexp=job.get_yearsexp_display()
        lines.append('Years of expirience: '+yearsexp)
        lines.append('Education: '+str(job.education))
        time=job.get_time_display()
        lines.append('Job Type: '+time)
        lines.append('Hybrid: '+str(job.hybrid))
        location=job.get_location_display()
        lines.append('Location: '+location)
        lines.append("================================")

    
    for i in range(len(lines)):
        if lines[i].startswith('Job Title:'):
            textob.setFont("Helvetica-Bold", 10)
        else:
            textob.setFont("Helvetica", 10)
        textob.textLine(lines[i])

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename="JobPriorityListPdf.pdf")


def jobsLocationPdfFile(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
   
    #c.saveState()
    #c.rotate(180)
    #c.drawImage(image, x=10, y=10, width=100, height=100)
    #c.restoreState()

    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica-Bold",10)
    
    image_path = 'C:\JHS_GROUP-36\static\jpg\LOGO.jpg'
    image = ImageReader(image_path)
    c.drawImage(image, x=200, y=-50, width=250, height=200)
    
    jobs=Upload.objects.all().order_by('location')
    lines=[" "," "," "," "," "," "," "]
    textob.setFont("Helvetica-Bold", 15)
    lines.append("Jobs by Locations Report")
    for job in jobs:
        lines.append("                                 ")
        textob.setFont("Helvetica-Bold", 12)
        lines.append('Job Title: '+job.title)
        textob.setFont("Helvetica-Bold", 10)
        lines.append('Sub Title: '+job.subTitle)
        textob.setFont("Helvetica", 10)
        lines.append(job.body)
        lines.append('Date of Publish: '+str(job.date))
        category = job.get_category_display()
        lines.append('Category: '+category)
        salaryRange = job.get_salaryRange_display()
        lines.append('Salary Range: '+salaryRange)
        yearsexp=job.get_yearsexp_display()
        lines.append('Years of expirience: '+yearsexp)
        education = job.get_education_display()
        lines.append('Education: '+education)
        time=job.get_time_display()
        lines.append('Job Type: '+time)
        lines.append('Hybrid: '+str(job.hybrid))
        location=job.get_location_display()
        lines.append('Location: '+location)
        lines.append("================================")

    
    for i in range(len(lines)):
        if lines[i].startswith('Job Title:') or lines[i].startswith('Location: '):
            textob.setFont("Helvetica-Bold", 10)
        else:
            textob.setFont("Helvetica", 10)
        textob.textLine(lines[i])

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename="JobLocationListPdf.pdf")

#generate textFileUploadList
def jobscsvFile(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=jobsList.csv'
    writer=csv.writer(response)
    
    jobs=Upload.objects.all().order_by('location')
    writer.writerow(['Job Title','subTitle','body','Category','Calary Range','Years Of Expirience','Education','Job Type','Hybrid ? ','Priority','Location','Available Amount'])
    for job in jobs:
        writer.writerow([job.title, job.subTitle, job.body, job.get_category_display(), job.get_salaryRange_display(), job.get_yearsexp_display(), job.get_education_display(), job.get_time_display(), job.hybrid, job.get_priority_display(), job.get_location_display(), job.availableAmount])
    return response


def Upload_list(request):
    uploads=Upload.objects.all()
    sort_form = SortForm()  # Create an instance of your form
    # Check if the form has been submitted
    if request.method == "POST":
        sort_form = SortForm(request.POST)  # Bind the form to the POST data
        if sort_form.is_valid():  # Check if the form is valid
            sort_field = sort_form.cleaned_data["sort_field"]  # Get the selected sort field
            sort_order = sort_form.cleaned_data["sort_order"]  # Get the selected sort order

            # Modify the queryset based on the selected sort field and order
            if sort_field == "title":
                if sort_order == "ascending":
                    uploads = uploads.order_by(Lower("title"))
                else:
                    uploads = uploads.order_by("-title")

            elif sort_field == "date":
                if sort_order == "ascending":
                    uploads = uploads.order_by(Lower("date"))
                else:
                    uploads = uploads.order_by("-date")

            elif sort_field == "salaryRange":
                if sort_order == "ascending":
                    uploads = uploads.order_by(Lower("salaryRange"))
                else:
                    uploads = uploads.order_by("-salaryRange")

            elif sort_field == "yearsexp":
                if sort_order == "ascending":
                    uploads = uploads.order_by(Lower("yearsexp"))
                else:
                    uploads = uploads.order_by("-yearsexp")

            elif sort_field == "time":
                if sort_order == "ascending":
                    uploads = uploads.order_by(Lower("time"))
                else:
                    uploads = uploads.order_by("-time")

            elif sort_field == "hybrid":
                if sort_order == "ascending":
                    uploads = uploads.order_by("hybrid")
                else:
                    uploads = uploads.order_by("-hybrid")

            elif sort_field == "location":
                if sort_order == "ascending":
                    uploads = uploads.order_by("location")
                else:
                    uploads = uploads.order_by("-location")
            
            elif sort_field == "viewsCounter":
                if sort_order == "ascending":
                    uploads = uploads.order_by("viewsCounter")
                else:
                    uploads = uploads.order_by("-viewsCounter")


    return render(request,'jobs/Upload_list.html',{'uploads':uploads,"sort_form": sort_form})

def uploadJob(request):
    submitted=False
    if request.method=="POST":
        form=UploadForm(request.POST)
        if form.is_valid():
            form.instance.slug = form.cleaned_data['title']
            emp=Employer.objects.get(username=request.user.username)
            form.instance.owner= emp  # set the owner_id field to the id of the currently 
            form.save()
            submitted=True
            return render(request,'jobs/success.html')
    else:
        form=UploadForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'jobs/uploadJob.html',{'form':form,'submitted':submitted})


def updateJob(request,upload_id):
    print(upload_id)
    job=Upload.objects.get(slug=upload_id)
    form=UploadForm(request.POST or None,instance=job)
    print(job.title)
    if form.is_valid():
        form.instance.slug = form.cleaned_data['title']
        form.save()
        print(request)
        return render(request,'jobs/success.html')
    return render(request,'jobs/updateJob.html',{'job':job,'form':form})

def job_details(request,slug):
    job=Upload.objects.get(slug=slug)
    job.viewsCounter+=1
    job.save()
    return render (request,'jobs/jobsDetails.html',{'job':job})

def success(request):
    return render(request,'jobs/success.html')

def deleteJob(request,upload_id):
    job=Upload.objects.get(slug=upload_id)
    job.delete()
    return render(request,'jobs/success.html',{'job':job})

def update_user(request, username):
    if request.method == 'POST':
        job_title=request.POST.get('jobtitle')
        print(job_title)
        # Update the statusforapplyjobs field for the user with the given username
        candidate = Candidate.objects.get(username=username)
        statusforapplyjobs = json.loads(candidate.statusforapplyjobs)
        print(statusforapplyjobs)

        jobi=candidate.applyjobs
        print(jobi)
        index = jobi.index(job_title)
        statusforapplyjobs[index]+=25
        status_list =candidate.statusforapplyjobs[index]
        candidate.statusforapplyjobs = json.dumps(statusforapplyjobs)
        print(candidate.statusforapplyjobs)
        candidate.save()
        return redirect('list')
    return render(request, 'jobsDetails.html')

def abort_user(request, username):
    if request.method == 'POST':
        job_title=request.POST.get('jobtitle')
        job=Upload.objects.get(title=job_title)
        candidate = Candidate.objects.get(username=username)
        job.applycandiadteuser.remove(candidate)

        statusforapplyjobs = json.loads(candidate.statusforapplyjobs)
        jobi=candidate.applyjobs
        index = jobi.index(job_title)
        statusforapplyjobs[index]=0
        candidate.statusforapplyjobs = json.dumps(statusforapplyjobs)
        print(candidate.statusforapplyjobs)
        candidate.save()
        job.save()
        return redirect('list')
    return render(request, 'jobsDetails.html')

def hired_user(request, username):
    if request.method == 'POST':
        job_title=request.POST.get('jobtitle')
        job=Upload.objects.get(title=job_title)
        candidate = Candidate.objects.get(username=username)
        job.applycandiadteuser.remove(candidate)

        statusforapplyjobs = json.loads(candidate.statusforapplyjobs)
        jobi=candidate.applyjobs
        index = jobi.index(job_title)
        statusforapplyjobs[index]=100
        candidate.statusforapplyjobs = json.dumps(statusforapplyjobs)
        candidate.save()
        job.save()
        return redirect('list')
    return render(request,'jobs/hired.html')

def applyCv(request,upload_id):
    job = get_object_or_404(Upload, slug=upload_id)
    cand=get_object_or_404(Candidate,username=request.user.username)
    job.applycandiadteuser.add(cand)
    applyjobs = set(cand.applyjobs)
    applyjobs.add(upload_id)
    cand.applyjobs = list(applyjobs)
    
    if cand.statusforapplyjobs:
        status_list = json.loads(cand.statusforapplyjobs)
    else:
        status_list = []
    status_list.append(25)
    cand.statusforapplyjobs = json.dumps(status_list)
    cand.save()
    job.save()
    return render(request,'jobs/success.html')

def candsta(request):
    return render(request, 'statusbar.html')

