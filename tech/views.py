
from django.shortcuts import render
from django.http import HttpResponse  
from .models import ticket
#from .functions import handle_uploaded_file  
from django.core.files import File


def ticket(request):
    #tickets=ticket.objects
    return render(request,'ticket.html')#,{'tickets':tickets})

#from .forms import Upload  
#def index(request):  
 #   if request.method == 'POST':  
  #      student = Upload(request.POST, request.FILES)
   # if student.is_valid():  
    #        handle_uploaded_file(request.FILES['file'])  
     #       return HttpResponse("File uploaded successfuly")  
   # else:  
    #    student = Upload()  
     #   return render(request,"index.html",{'form':student})  



