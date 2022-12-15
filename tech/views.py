
from django.shortcuts import render
from django.http import HttpResponse  
from .models import ticket
#from .functions import handle_uploaded_file  
from django.core.files import File



def ticket(request):
    #tickets=ticket.objects
    return render(request,'ticket.html')#,{'tickets':tickets})

#from .forms import StudentForm  
#def index(request):  
 #   if request.method == 'POST':  
  #      student = StudentForm(request.POST, request.FILES)
   # if student.is_valid():  
    #        handle_uploaded_file(request.FILES['file'])  
     #       return HttpResponse("File uploaded successfuly")  
   # else:  
    #    student = StudentForm()  
     #   return render(request,"index.html",{'form':student})  


def tech_main (request):
  return render(request,'tech_main.html')

def tech_approve_employer(request):
  context = {} 
  return render(request,'tech_approve_employer.html')