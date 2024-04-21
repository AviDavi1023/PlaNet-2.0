from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, world!")
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def upload(request):
    return render(request, 'upload.html', {})

def howtouse(request):
    return render(request, 'howtouse.html', {})