from django.shortcuts import render
from django.http import HttpResponseNotFound

def handler404(request, exception):
    return HttpResponseNotFound(render(request, '404.html'))