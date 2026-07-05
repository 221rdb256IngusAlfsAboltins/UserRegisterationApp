from django.urls import path

from . import views
urlpatterns = [
    path('',  views.homepage, name=""),
    path('registration',views.register, name="registration"),
    path('view-tasks', views.tasks, name="view-tasks"),
    path('create-task', views.create_task, name="create-task" ),
  
]
