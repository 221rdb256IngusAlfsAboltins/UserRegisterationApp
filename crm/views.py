from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.core.mail import send_mail
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

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
    

def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance= task)
        if form.is_valid():
            form.save()
            return redirect('view-tasks')
    else :
        form = TaskForm(instance=task)
        context = {'TaskForm': form}
        return render(request, 'crm/update-task.html', context)

def delete_task(request,id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('view-tasks')
    else:
        return HttpResponseForbidden("Access denied")
     
    