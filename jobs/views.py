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
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
#from .forms import JobApplicationForm
from django.contrib.auth.models import User
from users.models import Candidate

def jobsPdfFile(request):
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
    return FileResponse(buf,as_attachment=True,filename="JobListPdf.pdf")

#generate textFileUploadList
def jobscsvFile(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=jobsList.csv'
    writer=csv.writer(response)
    
    jobs=Upload.objects.all().order_by('location')
    writer.writerow(['Job Title','subTitle','body','Category','Calary Range','Years Of Expirience','Education','Job Type','Hybrid ? ','Priority','Location','Available Amount'])
    for job in jobs:
        writer.writerow([job.title, job.subTitle, job.body, job.category, job.salaryRange, job.yearsexp, job.education, job.time, job.hybrid, job.priority, job.location, job.availableAmount])
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


    return render(request,'jobs/Upload_list.html',{'uploads':uploads,"sort_form": sort_form})

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
    #job.update_views()
    #job=Upload.objects.filter(slug=slug.values())
    return render (request,'jobs/jobsDetails.html',{'job':job})

def success(request):
    return render(request,'jobs/success.html')

def deleteJob(request,upload_id):
    job=Upload.objects.get(slug=upload_id)
    job.delete()
    return render(request,'jobs/success.html',{'job':job})

def applyCv(request,upload_id):
    job = get_object_or_404(Upload, slug=upload_id)
    cand=get_object_or_404(Candidate,username=request.user.username)
    
    # Set the applycandiadteuser field to the request.user object
    job.applycandiadteuser.add(cand)
    applyjobs = set(json.loads(cand.applyjobs))
    applyjobs.add(upload_id)

    # Save the updated list back to the applyjobs field
    cand.applyjobs = json.dumps(list(applyjobs))
    cand.save()
    job.save()
    return render(request,'jobs/success.html')
"""
#def apply_for_job(request, job_id):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # create a new JobApplication object
            application = JobApplication(
                candidate_name=form.cleaned_data['name'],
                candidate_email=form.cleaned_data['email'],
                resume=form.cleaned_data['resume'],
                job_id=job_id
            )
            application.save()  # save the object to the database
            return redirect('jobs:success')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply.html', {'form': form})

"""