from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomePage(request):
    return render(request,'school/home.html')
    #return HttpResponse('<h1>HomePage</h1>')


def AboutPage(request):
    return render(request,'school/about.html')

def ContactUs(request):
    return render(request,'school/contact.html')