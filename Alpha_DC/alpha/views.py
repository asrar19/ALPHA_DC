from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.



def index(request : HttpRequest):
    return render(request, "alpha/index.html")


def home(request : HttpRequest):
    return render(request, "alpha/home.html")

def about(request : HttpRequest):
    return render(request, "alpha/about.html")
    
def contact(request : HttpRequest):
    return render(request, "alpha/contact.html")

def vision(request : HttpRequest):
    return render(request, "alpha/vision.html")

def services(request : HttpRequest):
    
    if request.method == "POST":
        nodes = request.POST["question1"]
        tier = request.POST["question2"]
        size = request.POST["question3"]
 
# main result 
        if nodes == "0-30" and tier == "1" and size == "small":
            return render(request, "alpha/services/service_1.html")

        elif nodes == "30-60" and tier == "2" and size == "medium":
            return render(request, "alpha/services/service_2.html")

        elif nodes == "60-90" and tier == "3" and size == "big":
            return render(request, "alpha/services/service_3.html")

        elif nodes == "90-120" and tier == "4" and size == "big":
            return render(request, "alpha/services/service_4.html")



    return render(request, "alpha/services.html")


