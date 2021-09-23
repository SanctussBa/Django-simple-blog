from django.http import HttpResponse #This is going to allow us to send a response to the user. When they requesta page, we are going to send them something.
from django.shortcuts import render #Allow us to render HTML template in the browser


def homepage(request):
    return render(request, "homepage.html")

def about(request):
    return render(request, "about.html")
