from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string

# Create your views here.


def homepage(request):
    months = ["january", "february", "march", "april"]
    response_data = render_to_string("challenges/homepage.html", {"months": months})
    return HttpResponse(response_data)

def show_month_challenge_by_number(request, month):
    if month == 1:
        rpath= reverse("month-challange", args=["january"])
        return HttpResponseRedirect(rpath)        
    elif month == 2:
        rpath= reverse("month-challenge", args=["february"])
        return HttpResponseRedirect(rpath)       
    elif month == 3:
        rpath= reverse("month-challenge", args=["march"])
        return HttpResponseRedirect(rpath)       
    elif month == 4:
        rpath= reverse("month-challenge", args= ["april"])
        return HttpResponseRedirect(rpath)        
    else:
        return HttpResponseNotFound("This month is not supported")
    


def show_month_challenge(request, month):
    challenge_text = ""
    if month == "january":
        challenge_text = "Eat healthy food"
    elif month == "february":
        challenge_text = "Walk for 20 minutes daily"
    elif month == "march":
        challenge_text = "Go to gym"
    elif month == "april":
        challenge_text = None
    else:
        return HttpResponseNotFound("This month is not supported")
    response_data = render_to_string(
        "challenges/ch.html", {"ch": challenge_text, "m": month}
    )
    return HttpResponse(response_data)
