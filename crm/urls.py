from django.urls import path

from . import views
urlpatterns = [
    path('',  views.homepage),
    path('home',  views.homepage),
    path('registration',views.register)
]
