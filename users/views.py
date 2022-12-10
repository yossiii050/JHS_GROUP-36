from django.http import HttpResponse # for recieve http response

def reg(request):
    return HttpResponse("This is a register page.")
