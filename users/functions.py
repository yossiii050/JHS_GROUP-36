from django.http import HttpResponse
def handle_uploaded_file(f):  
    with open('static/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    return HttpResponse("File uploaded successfully")
