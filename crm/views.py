from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.


def homepage(request):

    
    clientlist =[
    {
        "id":1,
        "name":'Jhon doe',
        "occupation":"elextical"
        
    }, {
        "id": 2,
        "name": 'Jhon doe',
        "occupation": "elextical"

    }]
    context = {'clientlist': clientlist}
    return render(request, 'crm/index.html',context)

def register(request):
    
  
    return render(request, 'crm/registration.html')
