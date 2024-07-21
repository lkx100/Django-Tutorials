from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome To HOME Page.\nHello World, Ready To learn Django!")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Welcome to About Page.\nThis response is coming from views.py file, where all the logical code is written")

def contact(request):
    return HttpResponse("Welcome to Contact Page.\nContact: lk5999950@gmail.com")