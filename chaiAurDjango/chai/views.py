from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import chaiVariety

# Create your views here.
def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, template_name = 'all_chai.html', context = {'chais': chais})

def order(request):
    return HttpResponse("This Order page is under Maintainance !")

def chai_details(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk = chai_id)    # pk: primary key
    return render(request, 'chai_details.html', {'chai': chai})