from django.urls import path
from .import views

urlpatterns = [
    path("HttpResponseHome/", views.home1),
    path("RenderFunctionHome/", views.home2, name="home2"),

    path("aboutmonth/<str:month>/", views.monthly_challenge_By_Str, name="month-detail"),
    path("activity_of_month/<str:month>/", views.favourite_activites_of_Month, name="month-activity"),

    path("<str:month>/<str:activity>/", views.detail_page_of_favourite_activity, name="activity-detial")

    # For Revering in template, We need two dynamic parameter for above path.
    # {% url "activity-detail"  month=Var1_passed_in_views.py   activity=Var2_passed_in_views.py %}
]
