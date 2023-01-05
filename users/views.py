from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from django.contrib.auth.forms import UserCreationForm #user create from django firms
from .forms import CreateEmployerForm,CreateCandidateForm,CandidateProfileForm
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import  redirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from .functions import handle_uploaded_file  
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test

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
    form=CreateEmployerForm()

    if request.method == 'POST':
        form=CreateEmployerForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form=CreateEmployerForm()
    context={'form':form}
    return render(request,'employerreg.html',context)

def candidateRegPage(request):
    if request.method == 'POST':
        candidate_form = CreateCandidateForm(request.POST)
        profile_form = CandidateProfileForm(request.POST)
        if candidate_form.is_valid() and profile_form.is_valid():
            user = candidate_form.save()
            profile = CandidateProfile(user=user, **profile_form.cleaned_data)
            profile.save()
            return redirect('login')
    else:
        candidate_form = CreateCandidateForm()
        profile_form = CandidateProfileForm()
    context = {'candidate_form': candidate_form, 'profile_form': profile_form}
    return render(request, 'candidatereg.html', context)


def candidateRegPage_old(request):
    form=CreateCandidateForm()

    if request.method == 'POST':
        form = CreateCandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context={'form':form}
    return render(request,'candidatereg.html',context)

def loginPage(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('home page')
        else:
            messages.info(request,'Username OR Password is incorrect')
            
    context={}
    return render(request,'login.html',context)

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
from .forms import UserUpdateForm

def view_groups(request):
    groups = Group.objects.filter(user=request.user)
    return render(request, 'template.html', {'groups': groups})

def Profile(request, username):
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

    return redirect("home page")