from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from .forms import EmployerSignUpForm,CandidateSignUpForm,CandidateEditProfileForm,EmployerEditProfileForm,CandidateProfileForm,CandidateForm,EmployerForm,EmployerProfile,EmployerProfileForm
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

from functools import wraps

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
        return JsonResponse({'message': 'User approved successfully'})
    return JsonResponse({'message': 'An error occurred while approving the user'}, status=400)

@user_passes_test(lambda u: u.is_staff)    
def approveEmp(request):
    form=User.objects.filter(is_active=False)
    print(form)
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

def employerRegPage(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
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
        form = CVForm(request.POST)
        if form.is_valid():
            new_form = CVFormModel(field=form.cleaned_data['field'], yearsexp=form.cleaned_data['yearsexp'], education=form.cleaned_data['education'], GitUrl=form.cleaned_data['GitUrl'])
            new_form.save()
            return HttpResponse("Form saved successfully")
        else:
            return render(request, "cv.html", {'form': form})
    else:  
        form = CVForm()  
        return render(request,"cv.html",{'form':form})


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
    print(user)
    #print(user.employer.is_employer)
    if request.user.username != user.username:
        return redirect('/')
    try:
        if user.employer.is_employer==True:
            employer = user.employer
            context = {'employer': employer}
            return render(request, 'employer_profile.html', context)
    except:
        if user.candidate.is_candidate==True:
            candidate = user.candidate
            print(candidate)
            context = {'candidate': candidate}
            return render(request, 'candidate_profile.html', context)
   


def edit_profile(request, username):
    user = get_object_or_404(User,username=username)
    print(user)
    try:
        if user.candidate.is_candidate==True:
            print("-----------"+user.candidate.candidate_id)
            return candidate_edit_profile(request, user.candidate.candidate_id)
    except:    
        if user.employer.is_employer==True:
            print("bababa")
            print( user.employer.employer_id)
            return employer_edit_profile(request, user.employer.employer_id)
    raise Http404   

def candidate_edit_profile(request, candidate_id):
    candidate = get_object_or_404(Candidate, candidate_id=candidate_id)
    #candidatebio = get_object_or_404(CandidateProfile, candidate=candidate)
    print(candidate)

    print("candidate is "+str(candidate))
    if request.method == 'POST':
        form1 = CandidateForm(request.POST, instance=candidate)
        print(form1.is_valid())

        if form1.is_valid():
            form1.save()
            return redirect('Profile', username=candidate.username) 
    else:
        form1 = CandidateForm(instance=candidate)
    return render(request, 'candidate_edit_profile.html', {'form1': form1, 'candidate': candidate})

def employer_edit_profile(request, employer_id):
    print("i get here")
    employer = get_object_or_404(Employer, employer_id=employer_id)
    print("here2")
    if request.method == 'POST':
        form1 = EmployerForm(request.POST, instance=employer)
        print(form1.is_valid())

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

"""def Profile(request, username):
    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        bio = user.userprofile.bio
        company_name=user.userprofile.company_name
        context = {'form': form, 'user': user, 'bio': bio, 'company_name': company_name}
        return render(request, 'profile.html', context)
    else:
        return redirect("home page")

def Profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = #UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('Profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error) 
    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        bio = user.userprofile.bio
        company_name=user.userprofile.company_name
 
        return render(request, 'profile.html', context={'form': form, 'user': user, 'bio': bio,'company_name':company_name})

    return redirect("home page")

def Profile_old(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('Profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error) 

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        bio = user.bio.bio
        form.fields['bio'].widget.attrs = {'rows': 1}
        return render(request, 'profile.html', context={'form': form, 'bio': bio})

    return redirect("home page")"""