from django.urls import path

from . import views
urlpatterns = [
    path('',  views.homepage, name=""),
    path('registration',views.register, name="registration"),
    path('view-tasks', views.tasks, name="view-tasks"),
    path('create-task', views.create_task, name="create-task" ),
    path('update-task/<str:id>', views.update_task, name="update-task"),
    path('delete-task/<str:id>', views.delete_task, name="delete-task"),
    path('my-login', views.my_login, name="my-login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('user-logout', views.user_logout,name="user-logout"),
]
