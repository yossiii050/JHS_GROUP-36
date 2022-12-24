from django.shortcuts import render

def paymentpage(request):
    return render(request,'paymentview.html')