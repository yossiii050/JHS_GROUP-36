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

def maintenance(request):
    if request.method == 'POST':
        # Get the password from the POST data
        password = request.POST.get('password')
        user = authenticate(request, username='admin', password=password)
        if user is not None:
            login(request, user)
            # Redirect the user to the home page
            MaintenanceMiddleware.maintenance_mode = False

            return redirect('home page site')
        else:
            # Return an error message if the password is incorrect
            error_message = 'Incorrect password'
    else:
        error_message = None
    # Render the maintenance page template
    return render(request, 'maintenance.html', {'error_message': error_message})
    
def home(request):
    if MaintenanceMiddleware.maintenance_mode:
        # Return the maintenance page template
        return redirect('maintenance')

        #return render(request, 'maintenance.html')
    else:
        # Return the regular home page template
        return render(request, 'home.html')

def toggle_maintenance_mode(request):
    # Toggle the maintenance mode flag in the middleware
    MaintenanceMiddleware.maintenance_mode = True
    # Redirect the user to the home page
    return redirect('maintenance')

