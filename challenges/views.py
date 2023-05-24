from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# Create your views here.


month_dict = {
    "january":"Eat no meat for the entire month k",
    "february": "Walk for at least 20 minutes a day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Eat no meat for the entire month k",
    "may": "Walk for at least 20 minutes a day",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Eat no meat for the entire month k",
    "august": "Walk for at least 20 minutes a day",
    "september": "Learn Django for at least 20 minutes every day",
    "october":"Eat no meat for the entire month k",
    "november" :"Walk for at least 20 minutes a day",
    "december": None
}


def index(request):
    months = list(month_dict.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    if month > len(month_dict):
        return HttpResponseNotFound("Invalid month")
    else:
        months = list(month_dict.keys())
        redirect_month = months[month -1]
        redirect_url = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        challenge_text = month_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()

