#from django.shortcuts import render

from django.http import HttpResponse # for recieve http response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")