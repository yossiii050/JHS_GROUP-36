from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from .forms import EmployerSignUpForm,CandidateSignUpForm,CandidateForm,EmployerForm,staffUserSignUpForm
from jobs.forms import SortForm
from tech.models import Ticket
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import  redirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout,get_user_model
from .functions import handle_uploaded_file  
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from jobs.models import Upload
from functools import wraps
from django.contrib.auth.forms import PasswordChangeForm
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

import io
from django.http import FileResponse



def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Check if the user's role is in the allowed list
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                # Redirect the user to the home page if they don't have the correct role
                return redirect('home')
        return wrapper
    return decorator

@user_passes_test(lambda u: u.is_staff)
def update_user_status(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()
        messages.info(request, 'User approved successfully')
        return redirect('approve_employers')
        #return JsonResponse({'message': 'User approved successfully'})
    return JsonResponse({'message': 'An error occurred while approving the user'}, status=400)

@user_passes_test(lambda u: u.is_staff)    
def approveEmp(request):
    form=User.objects.filter(is_active=False)
    context={'form':form}
    return render(request,'appr.html',context)

@user_passes_test(lambda u: u.is_staff)    
def ReportUsers(request):
    
    form=User.objects.all()
    context={'form':form}
    return render(request,'reportUser.html',context)
    
@user_passes_test(lambda u: u.is_staff)    
def ReportVIPUsers(request):
    User = get_user_model()
    vip_group = Group.objects.get(name='VIP')
    form = User.objects.filter(groups=vip_group)
    context={'form':form}
    return render(request,'reportVIPUsers.html',context)

@user_passes_test(lambda u: u.is_staff)    
def staffRegPage(request):
    if request.method == 'POST':
        form=staffUserSignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            is_staff=True)
            return redirect('techhome')
    else:
        form=staffUserSignUpForm()
    context={'form':form}        
    return render(request, 'staffReg.html',context)
    

def employerRegPage(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        #print(form.captcha)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'],
                                            is_active=False)

            employer = Employer.objects.create(user=user,
                                              email=form.cleaned_data['email'],
                                              username=form.cleaned_data['username'],
                                              CompanyName=form.cleaned_data['CompanyName'],
                                              employer_id=form.cleaned_data['employer_id'],)
            return redirect('login')
    else:
        form = EmployerSignUpForm()
       # print(form.captcha)
    context = {'form': form}
    return render(request, 'employerreg.html', context)

def candidateRegPage(request):
    if request.method == 'POST':
        form = CandidateSignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])

            candidate = Candidate.objects.create(user=user,
                                              email=form.cleaned_data['email'],
                                              username=form.cleaned_data['username'],
                                              first_name=form.cleaned_data['first_name'],
                                              last_name=form.cleaned_data['last_name'],
                                              candidate_id=form.cleaned_data['candidate_id'],
                                              date_of_birth=form.cleaned_data['date_of_birth'],
                                              phone_number=form.cleaned_data['phone_number'])

            return redirect('login')
    else:
        form=CandidateSignUpForm()
    context={'form':form}
    return render(request,'candidatereg.html',context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active ==False:
                messages.info(request, 'Your profile Not activated!')
                return redirect('login')
            login(request, user)
            return redirect('home page')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

from .models import CVFormModel
from .forms import CVForm  

def cv(request):  
    if request.method == 'POST':  
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = CVFormModel(field=form.cleaned_data['field'], yearsexp=form.cleaned_data['yearsexp'], education=form.cleaned_data['education'], GitUrl=form.cleaned_data['GitUrl'], file=request.FILES['file'])
            print(new_form)
            new_form.save()
            cand=Candidate.objects.get(username=request.user)
            cand.set_cv(new_form)
            cand.save()
            return redirect("Profile", request.user.username)
    else:
        form = CVForm()
    return render(request, 'cv.html', {'form': form})



def usershome(request):
    return render(request,'users.html')

from users.reports import registered_users_report

def registered_users(request):
    # Generate the report data
    data = registered_users_report()

    # Render the template with the report data
    return render(request, 'reports.html', data)

from django.contrib.auth.models import Group


def view_groups(request):
    groups = Group.objects.filter(user=request.user)
    return render(request, 'template.html', {'groups': groups})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    try:
        if user.employer.is_employer==True:
            employer = user.employer
            tick=Ticket.objects.all()
            job=Upload.objects.all()
            context = {'employer': employer,'tick':tick,'job':job}
            return render(request, 'employer_profile.html', context)
    except:
        if user.candidate.is_candidate==True:
            candidate = user.candidate
            candidatecv = candidate.cvcandidate
            jobs=Upload.objects.all()
            tick=Ticket.objects.all()
            
            context = {'candidate': candidate,'candidatecv': candidatecv,'tick':tick,'jobs':jobs}
            return render(request, 'candidate_profile.html', context)
   


def edit_profile(request, username):
    user = get_object_or_404(User,username=username)
    try:
        if user.candidate.is_candidate==True:
            return candidate_edit_profile(request, user.candidate.candidate_id)
    except:    
        if user.employer.is_employer==True:
            return employer_edit_profile(request, user.employer.employer_id)
    raise Http404   

def change_pass(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)

        if password_change_form.is_valid():
            password_change_form.save()
            return redirect('login') 
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'password_change_form': password_change_form})


def candidate_edit_profile(request, candidate_id):
    candidate = get_object_or_404(Candidate, candidate_id=candidate_id)
    if request.method == 'POST':
        form1 = CandidateForm(request.POST, instance=candidate)
        if form1.is_valid():
            form1.save()
            return redirect('Profile', username=candidate.username) 
    else:
        form1 = CandidateForm(instance=candidate)
    return render(request, 'candidate_edit_profile.html', {'form1': form1, 'candidate': candidate})

def employer_edit_profile(request, employer_id):
    employer = get_object_or_404(Employer, employer_id=employer_id)
    if request.method == 'POST':
        form1 = EmployerForm(request.POST, instance=employer)
        if form1.is_valid() :#and form2.is_valid():
            form1.save()            
            return redirect('Profile', username=employer.username) 
    else:
        form1 = EmployerForm( instance=employer)
    return render(request, 'employer_edit_profile.html', {'form1': form1, 'employer': employer})


def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home page')
    return render(request, 'delete_account_confirm.html')

def jobsList(request):
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


from .forms import ProgressForm

def CurrentStatus(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)

    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica-Bold", 15)

    image_path = 'C:\JHS_GROUP-36\static\jpg\LOGO.jpg'
    image = ImageReader(image_path)
    c.drawImage(image, x=200, y=-50, width=250, height=200)
    
    
    nominated=Candidate.objects.all()
    jobs=Upload.objects.all().order_by('date')
    lines=[" "," "," "," "]
    textob.setFont("Helvetica-Bold", 15)
    lines.append("Current Profile Status Report")

    for job in jobs:
        lines.append("                                 ")
        textob.setFont("Helvetica-Bold", 12)
        lines.append('Job Title: '+job.title)
        textob.setFont("Helvetica-Bold", 10)
        lines.append('Avialable Amount: '+ str(job.availableAmount))
        textob.setFont("Helvetica", 10)

        if job.applycandiadteuser.all() :
            lines.append("Candidate CV's on line: ")
            print(job.applycandiadteuser.all())
            for i in job.applycandiadteuser.all():
                print(i.username)
                lines.append("                                    "+i.username)
        
        for nominee in nominated:
            if nominee.applyjobs:
                print (nominee.applyjobs)
                for i in range (len(nominee.applyjobs)):
                    print(i)
                    if nominee.applyjobs[i]==job.title:
                        status_list = json.loads(nominee.statusforapplyjobs)
                        print(status_list)
                        if status_list[i]==25:
                            lines.append(nominee.username+" is 25% in The recruitment process ")
                        if status_list[i]==50:
                            lines.append(nominee.username+" is 50% in The recruitment process ")
                        if status_list[i]==75:
                            lines.append(nominee.username+" is 75% in The recruitment process ")
                        if status_list[i]==100:
                            lines.append(nominee.username+" is Hired! ")


                # for apply in nominee.applyjobs:
                #    if apply==job.title:


            
        lines.append("                                 ")
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
    return FileResponse(buf,as_attachment=True,filename="CurrentStatus.pdf")

