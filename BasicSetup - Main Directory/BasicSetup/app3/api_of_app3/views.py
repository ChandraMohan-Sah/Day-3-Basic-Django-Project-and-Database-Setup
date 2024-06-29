from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.urls import reverse
import json

'''
Challenge in app3
    1.List all months in home.html
        ->Each month should have encoded href tag so that if clicked we can go to its detail page.
        Two approaches for encoding href in an html doc:
          Approach 1:
                -
          
          Approach 2:
                -

    2.On clicking on any month it should show detail of that month.
        ->(on striking specific month like: "/month/january/"): How views.py should response;
        Approach 1:
            First prepare (response_data) in belows three format
                1.prepare hardcode html written in views.py.
                2.prepare html template using render_to_string() function.
                3.prepare html template using render() function.

                Above three response_data can be sent dirctly to client using  
                :-> return HttpResponse(response_data)

        Approach 2:
            First Prepare context to pass dictionary to html doc.
                -preparing key and value is pure python coding.

                Above (context) can be sent to html template using render() function.
                :-> return render(request,"app3/detailpage.html",context = {"key1":"value1", "key2":"value2"})
                            
'''
#--------------------------------------------------#
# For this small project it can be used as detail page : like for january , detail page ==> This month is January;

'''Actually these data should come from DATABASE'''
month_variable = {
    "january": "This month is January !",
    "february": "THis month is February !",
    "march": "THis month is March !",
    "april": "This month is april !",
    "may": "THis month is may!",
    "june": "THis month is june !",
    "july": "This month is July",
    "august": "This month is august",
    "september":"This month is september",
    "october":"This month is october",
    "november":"THsi month is november",
    "december":"This mointh is december"
}

month_activity = {
    "january": "football",
    "february": "Baseball",
    "march": "Cricket",
    "april": "Badminton",
    "may": "Calisthenics",
    "june": "Swimming",
    "july": "Tennis Ball",
    "august": "Gymming",
    "september":"Volleyball",
    "october":"Tug of War",
    "november":"Hide and Seek",
    "december":"Karate"
}

activity_detail = {
    "football": "Good for leg",
    "Baseball": "Good For focus",
    "Cricket": "Rest are all ok",
    "Badminton": "Rest are all ok",
    "Calisthenics": "Rest are all ok",
    "Swimming": "Rest are all ok",
    "Tennis Ball": "Rest are all ok",
    "Gymming": "Rest are all ok",
    "Volleyball": "Rest are all ok",
    "Tug of War": "Rest are all ok",
    "Hide and Seek": "Rest are all ok",
    "Karate": "Rest are all ok"
}


''' Rendering Content Using HttpResponse without any html templates'''
def home1(request):
    '''returning static content using HttpResponse : Nothing is sent to template yet'''
    # response_data1 = f"<h1>This is homepage</h1>"
    # static_content = response_data1
    # return HttpResponse(static_content)

    '''returning dynamic content using HttpResponse : Nothing is sent to template yet'''
    # months = list(month_variable.keys())
    # response_data1 = months
    # response_data2 = f"<ul>{months}</ul>"
    # dynamic_content = f"Response Data1: {response_data1} <br>Versus<br> Response Data2: {response_data2}"
    # return HttpResponse(dynamic_content)
    
    '''Method1 : returning dynamic content i.e just list all  month using HttpResponse : Nothing is sent to template yet'''
    # month_list = list(month_variable.keys())
    # resp1 = month_list[0]
    # resp2 = month_list[1]
    # resp3 = month_list[2]
    # resp4 = month_list[3]
    # dynamic_content = f"<ul>{resp1}</ul> <ul>{resp2}</ul><ul>{resp3}</ul><ul>{resp4}</ul>"
    # return HttpResponse(dynamic_content)

    ''' Method2 : returning dynamic content i.e just list all  month using HttpResponse : Nothing is sent to template yet'''
    # month_list = list(month_variable.keys())
    # dynamic_content = ""
    # for month in month_list:
    #     dynamic_content += f"<ul>{month}</ul>"
    # return HttpResponse(dynamic_content)

    ''' -----Created detailpage using this below approach------- '''
    '''returning dynamic content i.e 
        1.First list all month and relate it with href 
        2.Show detail of particular month using HttpResponse :
        Nothing is sent to template yet
    '''
    month_list = list(month_variable.keys())
    list_items = ""
    for month in month_list:
        month_path = reverse("month-detail", args=[month]) #url pattern creation and storing that url in a variable
        list_items += f"<li> <a href= \"{month_path}\">{month}</a></l1>" #relating all month to a particular url
        '''
        If "month-detail" resolves to /months/<month>/,the output would look like this:
        <ul>
            <li><a href="/months/January/"> January </a></li>
            <li><a href="/months/February/"> February </a></li>
            <li><a href="/months/March/"> March </a></li>
            ...
        </ul>
        '''
    response_data = f"<ul>{list_items}</ul>" #all list_items content have been stored in response_data
    dynamic_content = response_data
    return HttpResponse(dynamic_content)

#----------------------------------------------------------------------------------------------------------------------------------------------------------#


''' Rendering Content Using render() function  and using html templates for that'''

def home2(request):
    '''returning static content using render funtion : Template Used Here'''
    # return render(request, 'app3/1hellopage.html')


    '''returning dynamic content: {Just list all months} using render function : Template Used Here'''
    # month_list = list(month_variable.keys())
    # context ={
    #     "months": month_list
    # }
    # return render(request, 'app3/2listmonths.html', context)


    '''returning dynamic content: {list all months + show its detail on clicking it} using render function : Template Used Here'''
    month_list = list(month_variable.keys())
    context ={
        "months": month_list
    }
    return render(request, 'app3/3listmonths_and_show_detailpage.html', context)



#+---------Helper functions for  Detail Page of particular month----------------+#

# def monthly_challenge_By_Int(request, monthindex) ==> Can do easily see app2

def monthly_challenge_By_Str(request, month):
    try:
        month_text = month_variable[month]

        '''Approach 1 : Sending HttpResponse ; Plain text'''
        # return HttpResponse(month_text)


        '''Approach 2 : Sending Jsondata'''
        data = json.dumps(month_text)
        # return JsonResponse(data, safe=False) #In order to allow non-dict objects to be serialized set the safe parameter to False.


        '''Approach 2 : Sending Html Document'''
        context = {
            "month":month,
            "month_detail": month_text
        }
        return render(request, 'app3/4detailpage_instead_of_using_hardcoded_html_in_views.html', context)
    
    except:
        return HttpResponseNotFound("Invalid month passed as Second Argument")
    


def favourite_activites_of_Month(request, month):
    activity = month_activity[month]

    '''Approach 1: Plain text Response'''
    # return HttpResponse(activity)

    '''Approach 3: Sending Html Document'''
    context ={
        "month":month,
        "activity":activity 
    }
    return render(request, 'app3/5favourite_activites_of_particular_month.html', context)



def detail_page_of_favourite_activity(request, month, activity):
    particular_month = month
    particular_activity = month_activity[month]
    detail_activity = activity_detail[activity]
    
    context ={
        "particular_month": particular_month, # values are : january, february, march, april ...
        "activity": particular_activity,      # values are : football, Baseball, Cricket, Badminton ...
        "detail_activity": detail_activity    # values are : Good for leg, Good For focus ...
    }
    return render(request, "app3/6detailpage_favourite_activity.html", context)

#+---------------------------------------------------------------------------+#
