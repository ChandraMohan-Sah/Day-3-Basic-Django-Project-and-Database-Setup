from django.urls import path 
from .import views

urlpatterns = [

    #These are Static Urls
    path("january1/", views.january),
    path("february1/", views.February),
    path("march1/", views.March),

    #These are Dynamic Urls
    # path("<int:month>/", views.DynamicMonthsInteger), #integer passed as dynamic segment
    path("<int:monthindex>/", views.OptimizedDynamicMonthsInteger), #integer passed as dynamic segment

    # path("<str:month>/", views.DynamicMonthsString),     #string passed as dynamic segment
    path("<str:monthoptimized>/", views.OptimizedDynamicMonthsString, name="month-challenge"),#string passed as dynamic segment

]


