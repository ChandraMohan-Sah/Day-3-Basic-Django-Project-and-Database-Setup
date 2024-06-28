from django.urls import path 
from .import views 

urlpatterns = [
    path("app1indexpage/", views.index),
    path("app1home/",views.home)
    
]
