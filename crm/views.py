from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

from .forms import TaskForm,CreateUserForm,LogInForm


from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout

def homepage(request):

    
    return render(request, 'crm/index.html')

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
        else:
            context = {'CreateUserForm': form}
            return render(request, 'crm/registration.html', context)
    else:
        form = CreateUserForm()
        context = {'CreateUserForm': form}
        return render(request, 'crm/registration.html',context)
def my_login(request):
    
    if request.method == "POST":
        form = LogInForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
          
        context = {'LogInForm': form}
        return render(request, 'crm/my-login.html', context)
    else:
        form = LogInForm()
        context = {'LogInForm': form}
        return render(request, 'crm/my-login.html', context)
def user_logout(request):
    
   pass
    



def dashboard(request):
    return render(request, 'crm/dashboard.html')
  
  
  
  
    
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
     
    