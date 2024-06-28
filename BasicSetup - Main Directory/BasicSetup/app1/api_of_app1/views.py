from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is index page from app1.")


def home(request):
    # Example condition, replace this with your actual condition
    condition = True  # This should be your actual logic to check if the resource exists

    if not condition:
        # Resource not found, render custom 404 page
        return render(request, 'app1/custom404.html', status=404)
    
    # Resource found, render the actual template
    return render(request, 'app1/test.html')
