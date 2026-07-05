from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.core.mail import send_mail
from .forms import TaskForm


def homepage(request):

    
    return render(request, 'crm/index.html')

def register(request):
  
    return render(request, 'crm/registration.html')
def tasks(request):
    Tasks = Task.objects.all()
    context = {'Tasks': Tasks}
  
    return render(request,'crm/view-tasks.html', context )

def create_task(request):
    if request.method == "POST":
        form= TaskForm(request.POST)
        if form.is_valid()  :
            form.save()
            return redirect('view-tasks')
    else:
        form = TaskForm()
        context = {'TaskForm':form}
    return render(request, 'crm/create-task.html', context )