from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_chai(request):
    return render(request, template_name = 'all_chai.html')

def order(request):
    return HttpResponse("This Order page is under Maintainance !")