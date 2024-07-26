from django.shortcuts import render

# Create your views here.

def home(req): 
    return render(request = req, template_name = 'home.html', context = {'name': 'Default User'})

def add(req):
    a = int(req.POST['1st Number'])
    b = int(req.POST['2nd Number'])
    return render(request = req, template_name = 'add.html', context = {'Result': a+b})

def greet(req):
    name = req.POST['Name']
    return render(request = req, template_name = "greet.html", context = {"User": name})    # Context --> Passing arguments to html page to render variables