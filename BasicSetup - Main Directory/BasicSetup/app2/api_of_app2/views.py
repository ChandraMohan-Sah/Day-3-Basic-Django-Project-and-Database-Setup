from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
'''------Static Views : Function--------'''
def january(request):
    return HttpResponse("This is January page.")

def February(request):
    return HttpResponse("This is February Page")

def March(request):
    return HttpResponse("This is March Page")




'''-----------Dynamic Views : Function---------------------'''
#When string is passed as dynamic parameter
'''
def DynamicMonthsString(request, month):
    month_text = None
    if month == "january":
        month_text = "This is January Month"
    elif month == "february":
        month_text = "This is February Month"
    elif month == "march":
        month_text = "This is March Month"
    else:
        return HttpResponse("Invalid Month")
    return HttpResponse(month_text)
'''

#When integer is passed as dynamic parameter
def DynamicMonthsInteger(request, month):
    if month == 1:
        return HttpResponse("This is January Month")
    elif month == 2:
        return HttpResponse("This is February Month")
    elif month == 3:
        return HttpResponse("This is March Month")
    else:
        return HttpResponse("Invalid Month")
    

'''----------------Dynamic Views Optimized : Function---------------'''

challenge_dict ={
    "january": "This is January Month",
    "february": "This is February Month",
    "march": "This is March Month",
    "april": "This is April Month",
    "may": "This is May Month",
    "june": "This is June Month",
    "july": "This is July Month",
    "august": "This is August Month",
    "september": "This is September Month",
    "october": "This is October Month",
    "november": "This is November Month",
    "december": "This is December Month",
}

# When an integer is passed as a dynamic parameter
'''First Method'''
def OptimizedDynamicMonthsInteger(request, monthindex):
    months = list(challenge_dict.keys())

    if monthindex < 1 or monthindex > len(months):
        return HttpResponseNotFound("No value found")
    
    month_name = months[monthindex - 1]
    #return HttpResponseRedirect(f"/app2/{month_name}/")  # Adjust the redirect URL as needed

    '''Second Method'''
    #Not everytime we need to add args, But right now we need to add it as we have dynamic segment as well
    redirect_path = reverse("month-challenge", args=[month_name])
    return HttpResponseRedirect(redirect_path)


#When string is passed as dynamic parameter
def OptimizedDynamicMonthsString(request,monthoptimized):
    try:
        month_text = challenge_dict[monthoptimized]
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound("Invalid ")


















