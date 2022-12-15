
from django.shortcuts import render
from django.http import HttpResponse  
from .models import ticket
#from .functions import handle_uploaded_file  
from django.core.files import File
from django.template import loader


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


from sqlite3 import SQLITE_READ

