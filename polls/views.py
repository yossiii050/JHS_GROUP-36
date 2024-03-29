from django.http import HttpResponse
from django.shortcuts import render,redirect
from polls.maintenance_middleware import MaintenanceMiddleware,user_passes_test,maintenance_mode_active
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login

def home_page_view(*args, **kwargs):
    return HttpResponse("Hello")

def home_template(request):
    context={}
    return render(request,'home.html',context)

from jobs.models import Upload
def maintenance(request):
    if request.method == 'POST':
        # Get the password from the POST data
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and (user.is_staff or user.is_superuser):
            login(request, user)
            # Redirect the user to the home page
            MaintenanceMiddleware.maintenance_mode = False
            error_message = 'No Acsses,just for Admin'
            return redirect('home page site')
        elif user is not None:
            error_message = 'No Acsses,just for Admin'
        else:
            # Return an error message if the password is incorrect
            error_message = 'Incorrect password'
    else:
        error_message = None
    # Render the maintenance page template
    return render(request, 'maintenance.html', {'error_message': error_message})
from mysite.settings import BASE_DIR
def home(request):
    if MaintenanceMiddleware.maintenance_mode:
        # Return the maintenance page template
        return redirect('maintenance')

        #return render(request, 'maintenance.html')
    else:
        print("th"+str(BASE_DIR))
        job1=Upload.objects.all()
        notification_count=0
        for g in job1:
            notification_count+=g.applycandiadteuser.count()
        return render(request, 'home.html', {'job': job1, 'notification_count': notification_count})


def toggle_maintenance_mode(request):
    # Toggle the maintenance mode flag in the middleware
    MaintenanceMiddleware.maintenance_mode = True
    # Redirect the user to the home page
    return redirect('maintenance')

def movetoprofilebysuer(request):
    user=request.user
    print(user)
    if user.is_staff:
        return redirect('techhome')
    else:
        return redirect('Profile',username=user.username)
import copy
def clear_notifications(request):
    if request.user.is_authenticated:
        # Update the notification count in the database
        job1=Upload.objects.all()
        job2=job1.exclude(pk__in=job1)
        for g in job2:
            g.applycandiadteuser.clear()
    return redirect('home')