from django.http import HttpResponse
from django.shortcuts import render

def greet_message(request):
    return HttpResponse("Dummy Page !! He He")

def nextpage(request):
    return render(request, template_name = 'index.html', context = {'Name': 'Lucky Kumar'})